import requests
from flask import request

from .GastoClient import GastoClient
from .OrcamentoClient import OrcamentoClient


class Fachada:
    @staticmethod
    def get_gastos():
        return GastoClient.listar_gastos()

    @staticmethod
    def post_gasto(gasto):
        return GastoClient.cadastrar_gasto(gasto)

    @staticmethod
    def sync_gastos(info):
        return GastoClient.sincronizar_gastos(info)

    @staticmethod
    def create_orcamento(form):
        return OrcamentoClient.criar_orcamento(form)

    @staticmethod
    def get_orcamentos():
        return OrcamentoClient.listar_orcamentos()
