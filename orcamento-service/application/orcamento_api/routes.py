# application/orcamento_api/routes.py
from . import orcamento_api_blueprint
from .. import db
from ..models import Orcamento
from flask import make_response, request, jsonify


@orcamento_api_blueprint.route('/api/orcamentos', methods=['GET'])
def get_orcamentos():
    data = []
    for row in Orcamento.query.all():
        data.append(row.to_json())

    response = jsonify({'results': data})
    return response


@orcamento_api_blueprint.route('/api/orcamento/create', methods=['POST'])
def create_orcamento():
    orcamento = Orcamento()
    orcamento.nome = request.form['nome']
    orcamento.mes = request.form['mes']
    orcamento.valor_maximo = request.form['valor_maximo']

    db.session.add(orcamento)
    db.session.commit()

    response = jsonify({'message': 'Orcamento added',
                       'result': orcamento.to_json()})
    return response
