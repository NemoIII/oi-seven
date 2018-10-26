from flask import Blueprint, render_template, request, session
from .models import Enviar

app_page = Blueprint('app_page', __name__)
user_page = Blueprint('user_page', __name__)


@app_page.route('/')
@app_page.route('/index', methods=['GET', 'POST'])
def index():
	# form = EnviarForm()
	return render_template("index.html")


@user_page.route('/index', methods=['POST'])
def EnviarForm():
	form = EnviarForm()
	if request.method == 'POST' and form.validate():
		envio = Enviar(
			name=form.name.data,
			phone=form.phone.data,
			mobile=form.mobile.data
			)
		envio.save()
		return f"Obrigado por entrar em contato, {form.name.data}."
	return render_template("index.html", form=form)
