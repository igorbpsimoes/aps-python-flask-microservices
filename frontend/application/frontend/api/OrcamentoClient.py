# application/frontend/api/OrcamentoClient.py
import requests
from flask import request


class OrcamentoClient:
    @staticmethod
    def listar_orcamentos():
        r = requests.get('http://corcamento-service:5001/api/orcamentos')
        orcamentos = r.json()
        return orcamentos

    @staticmethod
    def criar_orcamento(payload):
        url = 'http://corcamento-service:5001/api/orcamento/create'
        response = requests.request("POST", url=url, data=payload)
        if response:
            orcamento = response.json()
        return orcamento
