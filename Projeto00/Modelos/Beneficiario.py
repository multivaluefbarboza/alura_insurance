from enum import Enum
from datetime import date
from Modelos.pessoa import pessoa


class TipoBeneficiario(Enum):
    PARENTE = 1
    AMIGO = 2
    OUTROS = 3
    FILHO = 4
    PAI = 5
    MAE = 6
    CONJUGE = 7


class beneficiario(pessoa):
    def __init__(self, nome: str, sobrenome: str, dataNascimento: date, cpf: str, rg: str, tipoBeneficiario: TipoBeneficiario, endereco: str, contato: str):

        super().__init__(nome, sobrenome, cpf, rg, dataNascimento, contato, endereco)

        self.__tipoBeneficiario = tipoBeneficiario
