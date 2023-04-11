# application/models.py
from . import db
from datetime import datetime


class Gasto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orcamento_id = db.Column(db.Integer, db.ForeignKey('orcamento.id'))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    nome = db.Column(db.String(255), nullable=False)
    valor = db.Column(db.Double, nullable=False)
    descricao = db.Column(db.String(255), nullable=True)
    data_ocorrida = db.Column(db.DateTime, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def to_json(self):
        return {
            'id': self.id,
            'orcamento_id': self.orcamento_id,
            'categoria_id': self.categoria_id,
            'nome': self.nome,
            'valor': self.valor,
            'descricao': self.descricao,
            'data_ocorrida': self.data_ocorrida
        }
