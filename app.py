import pymongo
from flask import Flask, jsonify, request
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

# JWT autentication
class Users(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

access = [
    Users(1, 'root', 'p7b623k'),
    Users(2, 'admin', 'p00p'),
]

ids_table   = {i.id: i for i in access}
names_table = {i.username: i for i in access}

def authenticate(username, password):
    user = names_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return ids_table.get(user_id, None)



# make database connection
def get_db(URI):
    client = pymongo.MongoClient(URI)
    return client.cryptongo

# Flask config
app =  Flask(__name__)
db_connection = get_db('mongodb://root:root@db:27017/')
app.config['SECRET_KEY'] = 'Oh8675s' 
app.config["JWT_SECRET_KEY"] = 'Oh8675s'
jwt = JWT(app, authenticate, identity)


# HomePage
@app.route('/api/')
def index():
    return jsonify( #Retornará una respuesta en formato json
		{
			'name': 'Cryptongo API',
            'Description':'This is a App that connects to CoinMarketCap API and save of the cryptocurrencies information in MongoDB database'
		}
	)

# Show items for names
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

# Show items with limits and names 
# Request EJ: /api/cryptos?limit=2&name=Bitcoin
@app.route('/api/cryptos')
def query_name_limit():
	name = request.args.get('name', '')
	limit = int(request.args.get('limit', 0))
	cursor = db_connection.tickers.find({'name':name}, {'_id': 0, 'ticker_hash': 0}).limit(limit)
	return jsonify(list(cursor))

# Count items in database
@app.route('/api/cryptos/info')
def information():
	cursor = db_connection.tickers.count()
	return jsonify( 
		{
			'Number of Documents': cursor,
			'Creation date': 'jun 19-2021 23:54',
            'Creator Name': 'Ovidio Andrade Zambrano'
		}
    )

#Delete Documents
# Request EJ: /api/cryptos/delete?name=Bitcoin
@app.route('/api/cryptos/delete',methods=['DELETE'])
@jwt_required()
def delete():
    name = request.args.get('name', '')
    cursor = db_connection.tickers.remove({'name':name})
    return jsonify( 
		{
			'Document delete': 'Success operation'
		}
    ) 



if __name__=='__main__':
    app.run()