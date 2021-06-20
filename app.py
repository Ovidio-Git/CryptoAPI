from os import name
import pymongo
from flask import Flask, jsonify, request


def get_documents():
	params = {}
	name = request.args.get('name', '')
	limit = int(request.args.get('limit', 0))
	if name:
		params.update({'name':name})
	cursor = db_connection.tickers.find(
		params, {'_id': 0, 'ticker_hash': 0}
        ).limit(limit)
	return list(cursor)

def get_db(URI):
    client = pymongo.MongoClient(URI)
    return client.cryptongo


app =  Flask(__name__)
db_connection = get_db('mongodb://root:root@db:27017/')

def model(Query):
    Data = { 
            'name': Query.name, 
            'symbol': Query.symbol, 
            'last_updated': Query.last_updated,
            'cmc_rank' : Query.cmc_rank,
            'quote': Query.quote
            }
    return Data

@app.route('/api/')
def index():
    return jsonify( #Retornará una respuesta en formato json
		{
			'name': 'Cryptongo API',
            'Description':'This is a App that connects to CoinMarketCap API and save of the cryptocurrencies information in MongoDB database'
		}
	)

# READ ITEMS FOR NAMES
@app.route('/api/cryptos/<name>')
def read_all(name):
    cursor = db_connection.tickers.find({"name":name}, {'_id': 0, 'ticker_hash': 0})
    response = list(cursor)
    if response != []:
        return jsonify(response)
    else:
        return jsonify( 
		{
			'Error': 'Cryptocurrency not found',
		}
	) 



if __name__=='__main__':
    app.run()