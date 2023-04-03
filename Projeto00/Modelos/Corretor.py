from datetime import date
from Modelos.pessoa import pessoa
 

class corretor(pessoa):
    def __init__(self, nome: str, sobrenome: str, dataNascimento: date, cpf: str, rg: str, endereco: str, contato: str, susep: str):

        super().__init__(nome, sobrenome, cpf, rg, dataNascimento, contato, endereco)

        self.__susep = susep
