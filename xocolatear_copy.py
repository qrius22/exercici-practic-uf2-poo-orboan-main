from pastisseria import Pastis
import copy

pastis_1 = Pastis(100)
pastis_2 = Pastis(120)
pastis_3 = Pastis(200)
pastis_4 = Pastis(160)
pastis_5 = Pastis(150)

pastissos= list()

pastissos.append(pastis_1)
pastissos.append(pastis_2)
pastissos.append(pastis_3)
pastissos.append(pastis_4)
pastissos.append(pastis_5)

for pastis in pastissos:
    print(pastis.xocolata)

def xocolatejar(pastis):
    pastis_copia = copy.copy(pastis)
    pastis_copia.xocolata = True
    return pastis_copia

pastis_amb_xocolata = list(map(xocolatejar, pastissos))

for pastis in pastissos:
    pastis_temporal = xocolatejar(pastis)
    pastis_amb_xocolata.append(pastis_temporal)
    
for pastis in pastissos:
    print(pastis.xocolata)
    
for pastis in pastis_amb_xocolata:
    print(pastis.xocolata)