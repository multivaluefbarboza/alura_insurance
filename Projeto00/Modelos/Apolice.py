from Modelos.Corretor import corretor
from Modelos.segurado import segurado
from datetime import datetime
from enum import Enum


class TipoApolice(Enum):
    VIDA = 1
    CARRO = 2


class StatusApolice(Enum):
    ATIVA = 1
    CANCELADA = 2
    LIQUIDADA = 3
    EM_SINISTRO = 4    


class apolice:
    def __init__(self, numero: int, tipo_apolice: TipoApolice, valorPremio:  float, segurado: segurado,
                 corretor: corretor, fim_vigencia: datetime, dataCriacao: datetime, status, valor_beneficio: float):
        self.__numero = numero
        self.__tipo = tipo_apolice
        self.__valorPremio = valorPremio
        self.__segurado = segurado
        self.__corretor = corretor
        self.__vigencia = fim_vigencia
        self.__dataCriacao = dataCriacao
        self.__status = status
        self.__valor_beneficio = valor_beneficio

    @property
    def Numero(self):
        return self.__numero
