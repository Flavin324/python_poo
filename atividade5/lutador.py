from abc import ABC

class Lutador(ABC):
    nome : str
    energia : float

    def __init__(self, n : int):
        self.nome = n
        self.energia = 100

    def soco(self, oponente):
        oponente.energia -= 5.5

    def __str__(self):
        return f"Nome: {self.nome} Energia: {self.energia}"

class Boxeador(Lutador):
    def cruzador(self, oponente : Lutador):
        oponente.energia -= 10.2

    def gancho(self, oponente : Lutador):
        oponente.energia -= 20.8

class Muay_Thai(Boxeador):
    def chute_alto(self, oponente : Lutador):
        oponente.energia -= 12.3

class Jujitsu(Lutador):
    def chave_braco(self, oponente : Lutador):
        oponente.energia -= 80

class MMA(Muay_Thai, Jujitsu):
    def superman_punch(self,oponente : Lutador):
        oponente.energia -= 50

    def chute_capoeira(self, oponente : Lutador):
        oponente.energia -= 22.13

