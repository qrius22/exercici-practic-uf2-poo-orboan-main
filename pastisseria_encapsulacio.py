class Pastis:
    def __init__(self, pes = 50, xocolata = False):
        self.pes = pes
        self.xocolata = xocolata

    @property #getter (lectura)
    def pes(self):
        return self.__pes
    
    @pes.setter #setter (escriptura)
    def pes(self, value):
        if value > 0:
            self.__pes = value
        else:
            print(f"{value} is invalid")

## Instanciació
pes = 150 #grams
pastis_1 = Pastis(pes)
pastis_2 = Pastis(pes)
pastis_3 = Pastis(200)
pastis_4 = Pastis()

print(type(pastis_1))
print(pastis_1.pes)

print(pastis_2.pes)
print(pastis_3.pes)
print(pastis_4.pes)

pastis_2 = Pastis(pes)
pastis_3 = Pastis(200)
pastis_xocolata = Pastis(200, True)

bossa = list()
bossa.append(pastis_2)
bossa.append(pastis_3)
bossa.append(pastis_xocolata)

for pastis in bossa:
    if pastis.xocolata == True:
        print("Xocolata!")

print(pastis_xocolata.pes)
print(f"pastis_xocolata és de xocolata? {pastis_xocolata.xocolata}")

print(pastis_2.pes)
pastis_2.pes = 300
print(pastis_2.pes)

pastis_2.pes = -50 #valor invàlid
print(pastis_2.pes)

class MyClass():
     def __init__(self):
             self.__superprivate = "Hello"
             self._semiprivate = ", world!"

