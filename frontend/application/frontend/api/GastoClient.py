# application/frontend/api/GastoClient.py
import requests
from flask import request


class GastoClient:
    @staticmethod
    def listar_gastos():
        r = requests.get('http://cgasto-service:5002/api/gastos')
        gastos = r.json()
        return gastos

    @staticmethod
    def cadastrar_gasto(gasto):
        url = 'http://cgasto-service:5002/api/gasto/create'
        response = requests.request("POST", url=url, data=gasto)
        if response:
            user = response.json()
            return user
        return

    @staticmethod
    def sincronizar_gastos(info):
        url = 'http://cgasto-service:5002/api/gasto/sincronizar'
        response = requests.request("POST", url=url, data=info)
        if response:
            user = response.json()
            return user
        return
