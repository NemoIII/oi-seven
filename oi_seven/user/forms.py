from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, ValidationError
from user.models import Enviar


class EnviarForm(FlaskForm):
	name = StringField("Seu nome", [validators.DataRequired(), validators.Length(min=4, max=30)])
	phone = IntegerField("Seu telefone + DDD", [validators.DataRequired(), validators.Length(min=10, max=11)])
	mobile = IntegerField("Seu celular + DDD", [validators.DataRequired(), validators.Length(min=10, max=12)])