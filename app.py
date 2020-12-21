from flask import Flask, render_template, url_for, redirect, request, jsonify
import pymongo
from pymongo import MongoClient
from flask_sqlalchemy import SQLAlchemy
import collections
import json

app = Flask(__name__)


cluster = MongoClient('mongodb://muradaghazada:885522@127.0.0.1:27017/mongo-database')
mdb = cluster['mongo-database']
collection = mdb['test']


# @app.route('/api/v1/get-data/<int:id>', methods=['GET', 'POST'])
# def get_data(id):


@app.route('/api/v1/send-data', methods=['GET', 'POST'])
def send_data():
    if request.method == 'POST':
        req = {'body': request.json}
        collection.insert_one(req)
        return jsonify(request.json)


if __name__ == "__main__":
    app.run(debug=True)