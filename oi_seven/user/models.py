from app import db
import datetime


class Enviar(db.Document):
	name = db.StringField(required=True)
	phone = db.IntegerField(required=True)
	mobile = db.IntegerField(required=True)
	created = db.DateTimeField(default=datetime.datetime.now)