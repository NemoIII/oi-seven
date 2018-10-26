from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators


class EnviarForm(FlaskForm):
	name = StringField("Nome\n", [validators.DataRequired(), validators.Length(min=4, max=30)])
	phone = IntegerField("Telefone + DDD\n", [validators.DataRequired(), validators.Length(min=10, max=11)])
	mobile = IntegerField("Celular + DDD\n", [validators.DataRequired(), validators.Length(min=10, max=12)])
