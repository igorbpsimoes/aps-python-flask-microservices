# application/frontend/api/ProductClient.py
import requests


class GastoClient:

    @staticmethod
    def get_gastos():
        r = requests.get('http://cgasto-service:5002/api/gastos')
        gastos = r.json()
        return gastos
