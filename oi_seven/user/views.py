from flask import Blueprint, render_template, request, redirect, url_for, Flask
from user.forms import EnviarForm
from user.models import Enviar

app_page = Blueprint('app_page', __name__)
user_page = Blueprint('user_page', __name__)

app = Flask(__name__)

# @user_page.route('/index', methods=['POST'])
@app_page.route('/')
@app_page.route('/index', methods=['GET', 'POST'])
def enviarForm():
	form = EnviarForm(request.form)
	error = None
	message = None
	number = list(range(1, 99999, 1))
	special_chars = ['!', '#', '@', ';', ':', ',', '*', '&', '%', '$']
	letra = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'w', 'x', 'y', 'z', 'll', 'ç']
	
	if request.method == 'POST':
		envio = Enviar(
			name=form.name.data.lower(),
			phone=form.phone.data,
			mobile=form.mobile.data
			)
		''' if form.name.data.contains(any(number)) or form.name.data.contains(any(special_chars)):
			error = "O nome deve conter apenas letras."
		if form.phone.data.contains(any(letra)) or form.mobile.data.contains(any(letra)):
			error = "Este campo deve conter apenas números."
		if not error:
			envio.save()
			message = f"Obrigado por entrar em contato, {form.name.data.lower()}."
			return message
		redirect(url_for('enviarForm'))'''
	return render_template("enviar_form.html", form=form, error=error, message=message)


if __name__ == '__main__':
	app.run(debug=True)


# def index():
# 	# form = EnviarForm()
# 	return render_template("index.html")
