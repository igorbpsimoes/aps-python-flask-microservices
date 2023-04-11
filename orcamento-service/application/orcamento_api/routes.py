# application/user_api/routes.py
from . import orcamento_api_blueprint
from .. import db, login_manager
from ..models import Orcamento
from flask import make_response, request, jsonify


@orcamento_api_blueprint.route('/api/orcamento', methods=['GET'])
def get_orcamentos():
    data = []
    for row in Orcamento.query.all():
        data.append(row.to_json())

    response = jsonify(data)
    return response


@orcamento_api_blueprint.route('/api/orcamento/create', methods=['POST'])
def create_orcamento():
    nome = request.form['nome']
    mes = request.form['mes']
    valor_maximo = request.form['valor_maximo']

    orcamento = orcamento()
    orcamento.nome = nome
    orcamento.mes = mes
    orcamento.valor_maximo = valor_maximo

    db.session.add(orcamento)
    db.session.commit()

    response = jsonify({'message': 'Orcamento added',
                       'result': orcamento.to_json()})

    return response

# @orcamento_api_blueprint.route('/api/orcamento/<username>/exists', methods=['GET'])
# def get_orcame(username):
#     item = User.query.filter_by(username=username).first()
#     if item is not None:
#         response = jsonify({'result': True})
#     else:
#         response = jsonify({'message': 'Cannot find username'}), 404
#     return response
