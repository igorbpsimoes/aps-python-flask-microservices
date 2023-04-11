# application/gasto_api/routes.py
from . import gasto_api_blueprint
from .. import db
from ..models import Gasto
from flask import jsonify, request


@gasto_api_blueprint.route('/api/gastos', methods=['GET'])
def listarGastos():
    gastos = []
    for gasto in Gasto.query.all():
        gastos.append(gasto.to_json())

    response = jsonify({'results': gastos})
    return response

@gasto_api_blueprint.route('/api/gastos/filter', methods=['GET'])
def filtrarGastos():
    orcamento_id  = request.args.get('orcamento_id', None)
    categoria_id  = request.args.get('categoria_id', None)
    data_inicio  = request.args.get('data_inicio', None)
    data_fim  = request.args.get('data_fim', None)

    gastos = []
    gasto_query = Gasto.query

    if orcamento_id is not None:
        gasto_query = gasto_query.filter(Gasto.orcamento_id == orcamento_id)

    if categoria_id is not None:
        gasto_query = gasto_query.filter(Gasto.categoria_id == categoria_id)

    if data_inicio is not None:
        gasto_query = gasto_query.filter(Gasto.data_ocorrida >= data_inicio)

    if data_fim is not None:
        gasto_query = gasto_query.filter(Gasto.data_ocorrida <= data_fim)

    for row in gasto_query.all():
        gastos.append(row.to_json())

    response = jsonify({'results': gastos})
    return response

@gasto_api_blueprint.route('/api/gasto/create', methods=['POST'])
def cadastrarGasto():
    gasto = Gasto()
    gasto.orcamento_id = request.form['orcamento_id']
    gasto.categoria_id = request.form['categoria_id']
    gasto.nome = request.form['nome']
    gasto.valor = request.form['valor']
    gasto.descricao = request.form['descricao']
    gasto.data_ocorrida = request.form['data_ocorrida']

    db.session.add(gasto)
    db.session.commit()

    response = jsonify({'message': 'Gasto added', 'gasto': item.to_json()})
    return response

@gasto_api_blueprint.route('/api/gasto/sincronizar', methods=['POST'])
def sincronizarGastos():
    json = request.get_json()

    usuario_cpf = json.get('usuario_cpf', '')
    data_comeco = json.get('data_comeco', '')
    data_fim = json.get('data_fim', '')

    url = 'https://6434029c582420e231716b14.mockapi.io/api/gastos'
    response = requests.get(url)

    if response is None:
        abort(404)

    gastos_inserir = []

    gastos = response.json()
    for gasto in gastos:
        novo_gasto = Gasto()
        novo_gasto.orcamento_id = gasto['orcamento_id']
        novo_gasto.categoria_id = gasto['categoria_id']
        novo_gasto.nome = gasto['nome']
        novo_gasto.valor = gasto['valor']
        novo_gasto.descricao = gasto['descricao']
        novo_gasto.data_ocorrida = gasto['data_ocorrida']

        gastos_inserir.append(novo_gasto)

    db.session.add_all(gastos_inserir)

    response = jsonify({'message': 'Gastos sincronizados'})
    return response

@gasto_api_blueprint.route('/api/gasto/<int:id>', methods=['DELETE'])
def removerGasto(id):
    gasto = Gasto.query.get(id)

    if gasto is None:
        abort(404)

    db.session.delete(gasto)
    db.session.commit()

    return jsonify({'result': True})

@app.route('/api/gasto/<int:id>', methods=['PUT'])
def editarGasto(id):
    if not request.json:
        abort(400)

    gasto = Gasto.query.get(id)
    if gasto is None:
        abort(404)

    gasto.orcamento_id = request.form['orcamento_id']
    gasto.categoria_id = request.form['categoria_id']
    gasto.nome = request.form['nome']
    gasto.valor = request.form['valor']
    gasto.descricao = request.form['descricao']
    gasto.data_ocorrida = request.form['data_ocorrida']

    db.session.commit()

    return jsonify(gasto.to_json())

@app.route('/api/gasto/<int:id>', methods=['PUT'])
def editarGasto(id):
    if not request.json:
        abort(400)

    gasto = Gasto.query.get(id)
    if gasto is None:
        abort(404)

    gasto.orcamento_id = request.form['orcamento_id']
    gasto.categoria_id = request.form['categoria_id']
    gasto.nome = request.form['nome']
    gasto.valor = request.form['valor']
    gasto.descricao = request.form['descricao']
    gasto.data_ocorrida = request.form['data_ocorrida']

    db.session.commit()

    return jsonify(gasto.to_json())
