# application/frontend/api/UserClient.py
import requests
from flask import session, request


class OrcamentoClient:
    @staticmethod
    def post_orcamento_create(form):
        payload = {
            'nome': form.nome.data,
            'mes': form.mes.data,
            'valor_maximo': form.valor_maximo.data
        }
        url = 'http://corcamento-service:5001/api/orcamento/create'
        response = requests.request("POST", url=url, data=payload)
        if response:
            orcamento = response.json()
        return orcamento

