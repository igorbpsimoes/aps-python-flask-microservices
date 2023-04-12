# application/frontend/views.py
import requests
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

    return render_template('gasto/index.html', gastos=gastos['results'], orcamentos=orcamentos['results'])


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
        return render_template('gasto/post_form.html', orcamentos=orcamentos['results'])

    return render_template("gasto/post_form.html")


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
        return render_template('gasto/sync_form.html')

    return render_template("gasto/sync_form.html")


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
