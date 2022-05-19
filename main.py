from unittest import result
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:6235@localhost/houses'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)

db.create_all()


class HouseModel(db.Model):
	__tablename__ = 'house_model'
	column1 = db.Column(db.Integer, primary_key=True)
	address = db.Column(db.String(100))
	price = db.Column(db.String(100))
	city = db.Column(db.String(100))
	title = db.Column(db.String(100))
	isbalconyglazed = db.Column(db.String(100))
	ceiling = db.Column(db.String(100))
	flatrenovation = db.Column(db.String(100))
	housetype = db.Column(db.String(100))
	year = db.Column(db.String(100))
	balcony = db.Column(db.String(100))
	bathroom = db.Column(db.String(100))
	residentialcomplex = db.Column(db.String(100))
	floor = db.Column(db.String(100))
	totalfloor = db.Column(db.String(100))
	area = db.Column(db.String(100))
    #realtor = db.Column(db.String(100))
	longitude = db.Column(db.String(100))
	latitude = db.Column(db.String(100))

	def __repr__(self):
		return f"{column1},{address},{price},{city},{title},{isbalconyglazed},{ceiling},{flatrenovation},{housetype},{year},{balcony},{bathroom},{residentialcomplex},{floor},{totalfloor},{area},{longitude},{latitude})"

resource_fields = {
	'column1': fields.Integer,
	'address': fields.String,
	'price': fields.String,
	'city': fields.String,
	'title': fields.String,
	'isbalconyglazed': fields.String,
	'ceiling': fields.String,
	'flatrenovation': fields.String,
	'housetype': fields.String,
	'year': fields.String,
	'bathroom': fields.String,
	'residentialcomplex': fields.String,
	'floor': fields.String,
	'totalfloor': fields.String,
	'area': fields.String,
	#'realtor': fields.String,
	'longitude': fields.String,
	'latitude': fields.String
}

class House(Resource):
	@marshal_with(resource_fields)
	def get(self, house_id):
		result = HouseModel.query.filter_by(column1=house_id).first()
		if not result:
			abort(404, message="Could not find video with that id")
		print("-----------------")
		print(result.column1)
		return result




api.add_resource(House, "/house/<int:house_id>")

if __name__ == "__main__":
	app.run(debug=True)
db.create_all()