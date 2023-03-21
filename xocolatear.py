from pastisseria_encapsulacio import Pastis
pastissos = list()

pastis_1 = Pastis(200)
pastis_2 = Pastis(800)
pastis_3 = Pastis(400)
pastis_4 = Pastis(100)
pastis_5 = Pastis(250)

pastissos = list()

#Append
pastissos.append(Pastis(pastis_1))
pastissos.append(Pastis(pastis_2))
pastissos.append(Pastis(pastis_3))
pastissos.append(Pastis(pastis_4))
pastissos.append(Pastis(pastis_5))

len(pastissos)

def xocolatejar(pastis):
    pastis.xocolata = True
    return pastis

for pastis in pastissos:
    xocolatejar(pastis)

#list(map(xocolatejar, pastissos_sense_xoco))

for pastis in pastissos:
    print(pastis.xocolata)
    






