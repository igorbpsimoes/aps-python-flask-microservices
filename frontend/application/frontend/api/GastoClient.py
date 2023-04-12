# application/frontend/api/GastoClient.py
import requests

class GastoClient:
    @staticmethod
    def listar_gastos():
        r = requests.get('http://cgasto-service:5002/api/gastos')
        gastos = r.json()
        return gastos
