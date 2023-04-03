from datetime import date
from Modelos.pessoa import pessoa
from Modelos.Beneficiario import beneficiario
from typing import List

class segurado(pessoa):
    def __init__(self, nome: str, sobrenome: str, dataNascimento: date, cpf: str, rg: str, endereco: str, contato: str,
                 beneficiarios:List[beneficiario]) :
         self.__beneficiario = beneficiarios
         self.__apolice = None

         super().__init__(nome, sobrenome,cpf, rg, dataNascimento, contato, endereco)

    @property
    def Nome(self):
        return self.__nome
