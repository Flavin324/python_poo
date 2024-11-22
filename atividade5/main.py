from lutador import *

popo = Boxeador("Popo")
bambam = Boxeador("Bambam")
Luigi = MMA("Luigi")


print(popo)
print(bambam)
print(Luigi)

popo.soco(bambam)
print(bambam)
popo.gancho(bambam)
print(bambam)
bambam.soco(popo)
print(popo)

gracie = MMA("Luigi")

popo.soco(Luigi)
Luigi.superman_punch(popo)
print(Luigi)

bronx = MMA("Carlos do Bronx")
bronx.superman_punch(Luigi)
print(Luigi)
