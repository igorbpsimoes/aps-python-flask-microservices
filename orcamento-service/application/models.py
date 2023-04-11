# application/models.py
from . import db
from datetime import datetime


class Orcamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), unique=True, nullable=False)
    mes = db.Column(db.DateTime, default=datetime.utcnow)
    valor_maximo = db.Column(db.Float, onupdate=datetime.utcnow)

    def to_json(self):
        return {
            'nome': self.nome,
            'mes': self.mes,
            'valor_maximo': self.valor_maximo,
            'id': self.id
        }
