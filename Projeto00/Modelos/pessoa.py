from datetime import date


class pessoa:
    def __init__(self, nome: str, sobrenome: str, cpf: str, rg: str, data_nascimento: date, contato: str, endereco: str):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__DataNascimento = data_nascimento
        self.__Cpf = cpf
        self.__RG = rg
        self.__Endereco = endereco
        self.__Contato = contato
