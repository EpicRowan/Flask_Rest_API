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

class ProductSchema(ma.Schema):
	class Meta:
		#fields that we want to show
		fields = ('id', 'name', 'description', 'price', 'qty')

#Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

#Create a product
@app.route('/product', methods=['POST'])
def add_product():
	name = request.json['name']
	description = request.json['description']
	price = request.json['price']
	qty = request.json['qty']

	new_product = Product(name, description, price, qty)

	db.session.add(new_product)
	db.session.commit()

	return product_schema.jsonify(new_product)

# @app.route('/', methods=['GET'])
# def get():
# 	return jsonify({'msg': "Hello!!!"})

app.secret_key = "supersecret"

if __name__ == '__main__':
	app.run(debug=True)