from abc import ABC, abstractmethod

class Funcionario(ABC):
    nome : str
    cpf : str
    __senha : int

    def __init__(self, nome: str , cpf : str , senha: int):
        self.nome = nome
        self.cpf = cpf
        self.__senha = senha

    @abstractmethod
    def autenticar(self, user : str, senha: int):
         pass

    def get_senha (self):
        return self.__senha

    def __str__(self):
        info = f'Nome: {self.nome}\n'
        info += f'Cpf:  {self.cpf}'
        return info

class Gerente(Funcionario):

    def autenticar(self, user: str, senha: int):
        if user == self.cpf and senha == self.get_senha():
            return True
        else:
            return False

    def cancelar_operacao(self):
        return "Operacao Cancelada!"


class Operador_caixa(Funcionario):
    numero_caixa : int

    def __init__(self, nome : str,cpf : str, senha : int, nc : int):
        super ().__init__(nome,cpf,senha)
        self.numero_caixa = nc

    def autenticar(self, user : str, senha: int):
        if user == str(self.numero_caixa) and senha == self. get_senha():
            return True
        else:
            return False

    def registrar_produto(self):
        return "Produto registrado!"

class Seguranca(Funcionario):
    posto : int

    def __init__(self, nome : str, cpf : str, senha : int, posto : int):
        super(). __init__(nome,cpf,senha)
        self.posto = posto


    def autenticar(self, user : str, senha : int):
        if user == str(self.posto) and senha == self. get_senha():
            return True
        else:
            return False

    def acionar_alarme(self):
        return"AAAAAAAAAAAHHHHHHHH"