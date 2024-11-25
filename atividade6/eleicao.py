import pickle
from typing import List
from atividade2.common import *
from interface import Transparencia
import csv
from gerenciarurna import *



class Urna(Transparencia):
    mesario : Pessoa
    __secao : int
    __zona : int
    __eleitores_presentes : List[Eleitor] = []
    __votos = {} #dicionario chave = numero do candidato, valor é a quantidade de votos

    def __init__(self, mesario : Pessoa, secao : int, zona : int,
                 candidatos : List[Candidato], eleitores : List[Eleitor]):
        self.mesario = mesario
        self.__secao = secao
        self.__zona = zona
        self.__nome_arquivo = f'{self.__zona}_{self.__secao}.pkl'
        self.__candidatos = candidatos
        self.__eleitores = []
        for eleitor in eleitores:
            if eleitor.zona == zona and eleitor.secao == secao:
                self.__eleitores.append(eleitor)

        for candidato in self.__candidatos:
            self.__votos[candidato.get_numero()] = 0
        self.__votos['BRANCO'] = 0
        self.__votos['NULO'] = 0

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def get_eleitor(self, titulo : int):
        for eleitor in self.__eleitores:
            if eleitor.get_titulo() == titulo:
                return eleitor
        return False

    def registrar_voto(self, eleitor : Eleitor, n_cand : int):
        self.__eleitores_presentes.append(eleitor)
        if n_cand in self.__votos:
            self.__votos[n_cand] += 1
        else:
            self.__votos['NULO'] += 1

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def __str__(self):
        info =  f'Urna da seção {self.__secao}, zona {self.__zona}\n'
        info += f'Mesario {self.mesario}\n'
        return info

    def to_csv(self):
        def to_csv(self):
            with open(f'{self.__secao}, {self.__zona}csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Seção', 'Zona','Titulo de Eleitor Presente'])

                for eleitor in self.__eleitores:
                    writer.writerow([self.__secao,self.__zona, eleitor.get_titulo()])
    def to_txt(self):
        with open(f'{self.__secao},{self.__zona}.txt', mode='w') as file:
            file.write((self.__str__()))

            for eleitor in self.__eleitores:
                file.write(f'{eleitor.get_titulo()}\n')

if __name__ == "__main__":
    c1 = Candidato("Zé daa manga","12312312", "213123-1", 43)
    c2 = Candidato("Maria", "32312370", "786868-2", 23)

    e1 = Eleitor("Maria", "2334334", "111111-2", 232323232, 458, 35)
    e2 = Eleitor("Jose","2323434","222334-4", 122122333, 234, 54)
    mesario = Eleitor("Joao","454636","33535-6", 1223445, 786, 60)
    urna = Urna(mesario, 252, 45,[c1, c2],[e1, e2])
    urna.to_csv()
    urna.to_txt()
