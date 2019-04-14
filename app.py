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

es = Elasticsearch(hosts="http://54.162.209.228:9200")


@app.route('/', methods=['GET'])
def introduction():
    print('Call made to introduction()')
    return 'This is TheLazyApp!'


@app.route('/users', methods=['GET'])
def get_users():
    content = request.args
    print(content)
    '''
    response = es.search(
        index='user',
        doc_type='users',
        body=content)
    '''
    if content['userrole'] == 'lazybob':
        users = [{
            "_id": "AWoam9-WYuK02M0NODA6",
            "role": "lazybob",
            "email": "abc@abc.com",
            "first_name": "Mita",
            "last_name": "Shimpi",
            "location": {
                "longitude": 0.0,
                "latitude": 0.0
            }
        }]
    if content['userrole'] == 'shopper':
        users = [{
            "_id": "AWoam9-WYuK00NODA6",
            "role": "shopper",
            "email": "abc@abc.com",
            "first_name": "Usmann",
            "last_name": "Usmann",
            "location": {
                "longitude": 0.0,
                "latitude": 0.0
            }
        }]

    # if response['hits']['total'] == 0:
    #    return []

    # users = [hit['_source'] for hit in response['hits']['hits']]
    return jsonify(users)


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
    content = request.get_json()
    user_id = content["user_id"]
    response = es.search(
        index='users',
        doc_type='user',
        body={"user_id": user_id, "status": 0})

    if response['hits']['total'] == 0:
        return []

    items = [hit['_source'] for hit in response['hits']['hits']]
    return items


@app.route('/cart', methods=['PUT'])
def put_in_cart():
    content = request.get_json()
    content["status"] = 0
    # items = [
    #     Item(item['name'], Store(item['store']['name'], item['store']['location']), item['price'], item['size'],
    #          item['description'], item['created_by']) for item in content['items']]
    es.index(index="item", body=content, doc_type="item")
    return "Cart updated"


@app.route('/order', methods=['PUT'])
def update_order():
    content = request.get_json()
    body = {
        "doc": {
            "status": 1
        }
    }
    es.update(index='item', doc_type='item', id=content['_id'], body=body)
    return 'Item added to order'


@app.route('/role', methods=['PUT'])
def update_role():
    content = request.get_json()
    body = {
        "doc": {
            "role": 1
        }
    }
    es.update(index='item', doc_type='item', id=content['_id'], body=body)
    return 'Item added to order'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

