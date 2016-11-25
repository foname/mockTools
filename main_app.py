import os
from flask import Flask, render_template
from pymongo import MongoClient
from flask_restful import Resource, Api
from mirror import mirror

app = Flask(__name__)
api = Api(app)

client = MongoClient(
    os.environ.get('DB_PORT_27017_TCP_ADDR', 'localhost'),
    27017)
db = client.mock_provider


@app.route('/')
def list():
    print(os.environ.get('DB_PORT_27017_TCP_ADDR', 'localhost'))
    _items = db.requests.find()
    items = [item for item in _items]
    print(items)
    return render_template('template.html', items=items)


class adapter(Resource):
    def get(self, provider_slug):
        item = db.requests.find_one({"request.urlPathMatching": "/{}".format(provider_slug), "request.method":"GET"})
        print(item)
        if item:
            return item['response']['jsonBody'], item['response']['status']
        return

    def post(self, provider_slug):
        item = db.requests.find_one({"request.urlPathMatching": "/{}".format(provider_slug), "request.method":"POST"})
        if item:
            return item['response']['jsonBody'], item['response']['status']
        return

    def put(self, provider_slug):
        item = db.requests.find_one({"request.urlPathMatching": "/{}".format(provider_slug), "request.method":"PUT"})
        if item:
            return item['response']['jsonBody'], item['response']['status']
        return



api.add_resource(mirror, '/mirror/<string:provider_slug>')
api.add_resource(adapter, '/<string:provider_slug>')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
