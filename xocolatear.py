<<<<<<< HEAD
from pastisseria import Pastis

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

print(pastis_1)

len(pastissos)

for pastis in pastissos:
    print(pastis.xocolata)

def xocolatejar(pastis):
    pastis.xocolata = True
    return pastis

for pastis in pastissos:
    xocolatejar(pastis)
    
print(pastis)
=======
from pastisseria import Pastis

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

print(pastis_1)

len(pastissos)

for pastis in pastissos:
    print(pastis.xocolata)

def xocolatejar(pastis):
    pastis.xocolata = True
    return pastis

for pastis in pastissos:
    xocolatejar(pastis)
    
print(pastis)
>>>>>>> 989062deff740e56d652cfc1d2603526cc0eba80
    