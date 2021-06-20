from os import write
import pymongo
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def coinmarket_API():
    # url to coinmarketcap API
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    # credentials for access to api
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '6cffef2a-0ed2-45fa-a390-0a59164df93f',
    }
    # send autentication credentials
    session = Session()
    session.headers.update(headers)
    try:
        # receive response from coinmarket API
        response = session.get(url)
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as error_api:
        print(error_api)
        


# create hash for data tickers unique indentification 
def get_hash(value):
    # import hash library
    from hashlib import sha512
    # create ticker with encrypt sha512
    return sha512(value.encode('utf-8')).hexdigest()


# get first element key
def first_element(elements):
    return elements[0]


# order information for get hash unique of each ticker
def get_ticker_hash(ticker_data):
    from collections import OrderedDict
    # order data for items of ticker data
    ticker_data = OrderedDict(
        sorted(
            ticker_data.items(),
            key = first_element
        )
    )

    ticker_value = ''
    # data {key, value}
    for _, value in ticker_data.items():
        # save values of ticker
        ticker_value += str(value)

    return get_hash(ticker_value)


# create data base cryptongo
def get_db(link):
    client = pymongo.MongoClient(link)
    return client.cryptongo


#  function for check if data exists in mongo database using ticker_hash 
def check_if_exists(db_connection, ticker_data):
    ticker_hash = get_ticker_hash(ticker_data)
    if db_connection.tickers.find_one({'ticker_hash': ticker_hash}):
        return True
    else:
        return False


# save information to coinmarket in mongoDB
def save_crypto(db_connection, ticker_data=None):

    del ticker_data['id']
    del ticker_data['tags']
    del ticker_data['slug']
    del ticker_data['platform']
    
    # verifiation if ticker_data not exists
    if not ticker_data:
        return False
    # check if data exists in mongo database 
    elif check_if_exists(db_connection, ticker_data):
        return False


    ticker_hash = get_ticker_hash(ticker_data)
    # create ticker hash field in ticker data documents
    ticker_data['ticker_hash'] = ticker_hash
    db_connection.tickers.insert_one(ticker_data)
    return True


def run():
    # connecting to MongoDB
    connection = get_db('mongodb://root:root@db:27017/')
    # save coinmarket API data in tickers
    # tickers = coinmarket_API()

    with open('data.txt') as json_file:
        data = json.load(json_file)
    tickers = data
    # delete status key
    del tickers['status']
    # save coinmarket API data in MongoDB
    for ticker in tickers['data']:
        save_crypto(connection, ticker)
    print("Data save in MongoDB")
    



if __name__=='__main__':
    run()
