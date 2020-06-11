from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)

# make sure we can correcly locate the db file
basedir =os.path.abspath(os.path.dirname(__file__))

# will look for a db called sqlite in current folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFCAITONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True)
	description = db.Column(db.String(200))
	price = db.Column(db.Float)
	qty = db.Column(db. Integer)

	def __init__(self, name, description, price, qty):
		self.name = name
		self.description = description
		self.price = price
		self.qty = qty 



# @app.route('/', methods=['GET'])
# def get():
# 	return jsonify({'msg': "Hello!!!"})

app.secret_key = "supersecret"

if __name__ == '__main__':
	app.run(debug=True)