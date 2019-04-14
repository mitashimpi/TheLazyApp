from flask import Flask
from flask import request
from flask import jsonify
from elasticsearch import Elasticsearch
from userrole import UserRole
from item import Item
from user import User
from location import Location
from store import Store

app = Flask(__name__)

es = Elasticsearch("http://54.162.209.228:9200")
es.indices.create(index='user', ignore=400)


@app.route('/', methods=['GET'])
def introduction():
    print('Call made to introduction()')
    return 'This is TheLazyApp!'


@app.route('/users', methods=['GET'])
def get_users():
    args = request.args
    print(args)  # For debugging
    user = UserRole(args['userrole'])
    if user is UserRole.LAZYBOB:
        print('User is ' + str(user))
    elif user is UserRole.SHOPPER:
        print('User is a ' + str(user))
    users = [
  {
    "email": "abc@abc.com",
    "first_name": "Yuka",
    "last_name": "Black",
    "location": {
      "longitude": 0,
      "latitude": 0
    }
  }
]

    return jsonify(users)


@app.route('/users', methods=['PUT'])
def update_users():
    print('Adding/Updating user')
    content = request.get_json()
    users = [User(user['first_name'], user['last_name'], user['email'],
                  Location(user['location']['longitude'], user['location']['latitude'])) for user in content['users']]
    return 'User updated'


@app.route('/cart', methods=['GET'])
def get_from_cart():
    cart = {
	"items": [
		{
			"name": "Ice-cream",
			"description": "Ice-cream is cold",
			"store": {
				"name": "Target",
				"location": {
					"longitude": 0.0,
					"latitude": 0.0
				}
			},
			"price": 3.00,
			"size": "Small",
			"created_by": 1
		}
		]
}
    print('Cart is mocked!')
    return jsonify(cart)


@app.route('/cart', methods=['PUT'])
def put_in_cart():
    content = request.get_json()
    items = [
        Item(item['name'], Store(item['store']['name'], item['store']['location']), item['price'], item['size'],
             item['description'], item['created_by']) for item in content['items']]
    print(items)
    return "Cart updated"


@app.route('/order', methods=['PUT'])
def update_order():
    content = request.get_json()
    body = {
        "doc": {
            "@status": 1
        }
    }
    es.update(index='item', doc_type='item', id=content['_id'], body=body)
    return 'Item added to order'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

