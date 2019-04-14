from flask import Flask
from flask import request
from elasticsearch import Elasticsearch
from userrole import UserRole
from item import Item
from user import User
from location import Location
from store import Store

app = Flask(__name__)

es = Elasticsearch(hosts="http://54.162.209.228:9200")
es.indices.create(index='user', ignore=400)


@app.route('/', methods=['GET'])
def introduction():
    print('Call made to introduction()')
    return 'This is TheLazyApp!'


@app.route('/users', methods=['GET'])
def get_users():
    args = request.args
    print(args)  # For debugging
    user = UserRole(args['user_type'])
    if user is UserRole.LAZYBOB:
        print('User is ' + str(user))
    elif user is UserRole.SHOPPER:
        print('User is a ' + str(user))
    return "User: " + str(user)


@app.route('/users', methods=['PUT'])
def update_users():
    content = request.get_json()

    # print("content:", content)
    # user = content['first_name'], content['last_name'], content['email'], content['created_at'],
    #               Location(user['location']['longitude'], user['location']['latitude']
    es.index(index="user", body=content, doc_type="users")
    return 'User added/updated successfully'


@app.route('/cart', methods=['GET'])
def get_from_cart():
    print('Cart is empty!')
    return "Empty cart!"


@app.route('/cart', methods=['PUT'])
def put_in_cart():
    content = request.get_json()
    content["status"] = 0
    # items = [
    #     Item(item['name'], Store(item['store']['name'], item['store']['location']), item['price'], item['size'],
    #          item['description'], item['created_by']) for item in content['items']]
    es.index(index="item", body=content, doc_type="item")
    return "Cart updated"


@app.route('/order', methods=['GET'])
def get_order_details():
    return 'No order details available'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

