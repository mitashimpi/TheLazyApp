from flask import Flask
from flask import request
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
    user = UserRole(args['user_type'])
    if user is UserRole.LAZYBOB:
        print('User is ' + str(user))
    elif user is UserRole.SHOPPER:
        print('User is a ' + str(user))
    return "User: " + str(user)


@app.route('/users', methods=['PUT'])
def update_users():
    print('Adding/Updating user')
    content = request.get_json()
    users = [User(user['first_name'], user['last_name'], user['email'], user['created_at'],
                  Location(user['location']['longitude'], user['location']['latitude'])) for user in content['users']]
    print(users)
    return 'User added/updated successfully'


@app.route('/cart', methods=['GET'])
def get_from_cart():
    print('Cart is empty!')
    return "Empty cart!"


@app.route('/cart', methods=['PUT'])
def put_in_cart():
    content = request.get_json()
    items = [
        Item(item['name'], Store(item['store']['name'], item['store']['location']), item['price'], item['size'],
             item['description'], item['created_by']) for item in content['items']]
    print(items)
    return "Cart updated"


@app.route('/order', methods=['GET'])
def get_order_details():
    return 'No order details available'


# ---------------------------------------------------------------------------------------------------------------------
'''
class Introduction(Resource):
    def get(self):
        print("Call made to introduction()")
        return 'This is TheLazyApp!'


class FindUsers(Resource):
    def get(self):
        args = request.args
        print(args)  # For debugging
        user = User(args['user_type'])
        if user is User.LAZYBOB:
            print('User is ' + str(user))
        elif user is User.SHOPPER:
            print('User is a ' + str(user))
        return "User: " + str(user)


class Cart(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('items', type=str, location='json')
        super(Cart, self).__init__()

    def put(self):
        args = request.getjson()
        print(args)
        print('Adding to cart')

    def get(self):
        print('Cart is empty!')


api.add_resource(Introduction, '/')
api.add_resource(FindUsers, '/find')
api.add_resource(Cart, '/cart')

'''

if __name__ == '__main__':
    app.run()