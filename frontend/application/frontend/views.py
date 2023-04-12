# application/frontend/views.py
import requests
from . import forms
from . import frontend_blueprint
from .api.Fachada import Fachada
from flask import render_template, session, redirect, url_for, flash, request


@frontend_blueprint.route('/', methods=['GET'])
def home():

    try:
        gastos = Fachada.get_gastos()
        orcamentos = Fachada.get_orcamentos()
    except requests.exceptions.ConnectionError:
        gastos = {
            'results': []
        }

    return render_template('home/index.html', gastos=gastos['results'], orcamentos=orcamentos['results'])


@frontend_blueprint.route('/criar-gasto', methods=['GET', 'POST'])
def criar_gasto():

    if request.method == 'POST':

        payload = {
            'nome': request.form.get('nome'),
            'data_ocorrida': request.form.get('data_ocorrida'),
            'valor': request.form.get('valor'),
            'descricao': request.form.get('descricao'),
            'orcamento_id': request.form.get('orcamento_id')
        }

        Fachada.post_gasto(payload)

    elif request.method == 'GET':
        orcamentos = Fachada.get_orcamentos()
        return render_template('home/gasto_form.html', orcamentos=orcamentos['results'])

    return render_template("home/gasto_form.html")


@frontend_blueprint.route('/sincronizar-gastos', methods=['GET', 'POST'])
def sincronizar_gastos():

    if request.method == 'POST':

        payload = {
            'usuario_cpf': request.form.get('usuario_cpf'),
            'data_inicio': request.form.get('data_inicio'),
            'data_fim': request.form.get('data_fim')
        }

        Fachada.sync_gastos(payload)

    elif request.method == 'GET':
        return render_template('home/sync_form.html')

    return render_template("home/sync_form.html")


@frontend_blueprint.route('/cadastrar-orcamento', methods=['GET', 'POST'])
def cadastrar_orcamento():
    if request.method == 'POST':

        payload = {
            'nome': request.form.get('nome'),
            'mes': request.form.get('mes'),
            'valor_maximo': request.form.get('valor_maximo')
        }

        Fachada.create_orcamento(payload)

    elif request.method == 'GET':
        return render_template('orcamento/form.html')

    return render_template("orcamento/form.html")


@frontend_blueprint.route('/orcamento', methods=['GET'])
def home_orcamento():
    try:
        orcamentos = Fachada.get_orcamentos()
    except requests.exceptions.ConnectionError:
        orcamentos = {
            'results': []
        }

    return render_template('orcamento/index.html', orcamentos=orcamentos['results'])


'''
@frontend_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            username = form.username.data

            # Search for existing user
            user = UserClient.does_exist(username)
            if user:
                # Existing user found
                flash('Please try another username', 'error')
                return render_template('register/index.html', form=form)
            else:
                # Attempt to create new user
                user = UserClient.post_user_create(form)
                if user:
                    flash('Thanks for registering, please login', 'success')
                    return redirect(url_for('frontend.login'))

        else:
            flash('Errors found', 'error')

    return render_template('register/index.html', form=form)


@frontend_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('frontend.home'))
    form = forms.LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            api_key = UserClient.post_login(form)
            if api_key:
                session['user_api_key'] = api_key
                user = UserClient.get_user()
                session['user'] = user['result']

                order = OrderClient.get_order()
                if order.get('result', False):
                    session['order'] = order['result']

                flash('Welcome back, ' + user['result']['username'], 'success')
                return redirect(url_for('frontend.home'))
            else:
                flash('Cannot login', 'error')
        else:
            flash('Errors found', 'error')
    return render_template('login/index.html', form=form)

@frontend_blueprint.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('frontend.home'))


@frontend_blueprint.route('/checkout', methods=['GET'])
def summary():
    if 'user' not in session:
        flash('Please login', 'error')
        return redirect(url_for('frontend.login'))

    if 'order' not in session:
        flash('No order found', 'error')
        return redirect(url_for('frontend.home'))
    order = OrderClient.get_order()

    if len(order['result']['items']) == 0:
        flash('No order found', 'error')
        return redirect(url_for('frontend.home'))

    OrderClient.post_checkout()

    return redirect(url_for('frontend.thank_you'))

@frontend_blueprint.route('/order/thank-you', methods=['GET'])
def thank_you():
    if 'user' not in session:
        flash('Please login', 'error')
        return redirect(url_for('frontend.login'))

    if 'order' not in session:
        flash('No order found', 'error')
        return redirect(url_for('frontend.home'))

    session.pop('order', None)
    flash('Thank you for your order', 'success')

    return render_template('order/thankyou.html')
'''
