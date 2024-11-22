from abc import ABC, abstractmethod

class Golpe(ABC):
    @abstractmethod
    def golpear(self, j):
        pass

class Soco(Golpe):
    def golpear(self, j):
        j.energia -= 1

class Chute(Golpe):
    def golpear(self, j):
        j.energia -= 2






