import requests
from flask import request

from .GastoClient import GastoClient
from .OrcamentoClient import OrcamentoClient

class Fachada:
  @staticmethod
  def get_gastos():
    return GastoClient.listar_gastos()

  @staticmethod
  def create_orcamento(form):
    return OrcamentoClient.criar_orcamento(form)
