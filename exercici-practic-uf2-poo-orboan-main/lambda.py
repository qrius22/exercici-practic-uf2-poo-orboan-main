def suma(x,y):
    return x + y
print(suma(4,6))
#Suma, Resta
resta = lambda x,y: x- y
print(resta(10,4))

    
#Functions are first class Citizens

def calcula(x,y,operacio):
    return operacio(x,y)

print(calcula(3,8,suma))
print(calcula(8,3,resta))
print(calcula(2,5,lambda x,y: x*y))
