from flask import Flask, render_template, url_for, redirect, request, jsonify
# from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy
import collections
import json

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


# app.config['MONGODB_SETTINGS'] = {
#     'db': 'my_database',
#     'host': 'localhost',
#     'port': 27017
# }
# db = MongoEngine()
# db.init_app(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    number = db.Column(db.Integer)

    def __init__(self, first_name, last_name, number):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number


class UserSerializer:
    def __init__(self, user):
        self.user = user


    def to_dict(self):
        return collections.OrderedDict([
            ('id', self.user.id),
            ('first_name', self.user.first_name),
            ('last_name', self.user.last_name),
            ('number', self.user.number)
        ])


@app.route('/api/v1/adduser', methods=['GET', 'POST'])
def adduser():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        number = request.form['number']
        user = Person(first_name, last_name, number)
        db.session.add(user)
        db.session.commit()
        return jsonify({"success": "success"})

@app.route('/api/v1/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = Person.query.all()
        serialized = [UserSerializer(user).to_dict() for user in users]
        return jsonify(serialized)
    elif request.method == 'POST':
        first_name = json.loads(request)
        print(first_name)
        users = Person.query.filter_by(first_name=first_name)
        # users = Person.query.all()
        print(users)
        serialized = [UserSerializer(user).to_dict() for user in users]
        return jsonify(serialized)


@app.route('/send-request', methods=['GET', 'POST'])
def sendrequest():
    return render_template('request.html')


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)