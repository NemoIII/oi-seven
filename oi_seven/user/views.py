from flask import Blueprint, render_template, request
from user.forms import EnviarForm
from user.models import Enviar

app_page = Blueprint('app_page', __name__)
user_page = Blueprint('user_page', __name__)


# @user_page.route('/index', methods=['POST'])
@app_page.route('/')
@app_page.route('/index', methods=['GET', 'POST'])
def enviarForm():
	form = EnviarForm(request.form)
	if request.method == 'POST' and form.validate():
		envio = Enviar(
			name=form.name.data,
			phone=form.phone.data,
			mobile=form.mobile.data
			)
		envio.save()
		return f"Obrigado por entrar em contato, {form.name.data}."
	return render_template("enviar_form.html", form=form)



# def index():
# 	# form = EnviarForm()
# 	return render_template("index.html")
