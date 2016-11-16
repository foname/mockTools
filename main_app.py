import os
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    os.environ.get('DB_PORT_27017_TCP_ADDR','localhost'),
    27017)

db = client.requests

@app.route('/')
def todo():

    _items = db.requests.find()
    items = [item for item in _items]

    return render_template('template.html', items=items)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)