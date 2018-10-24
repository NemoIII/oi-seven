from app import db
import datetime


class Enviar(db.Document):
	name = db.StringField(required=True)
	phone = db.IntField(required=True)
	mobile = db.IntField(required=True)
	created = db.DateTimeField(default=datetime.datetime.now)
