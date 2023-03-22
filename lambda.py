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

my_list = [12,65,54,39,102,339,221,50,70]

#use anonymous function to filter and comparing
#if divisible or not 
result = list(filter(lambda x: (x % 2== 0), my_list))

# Printing the result
print(result)



#def startsWithWove1(nom): 
#    for nom in name:
#        if nom.startswith("AEIOU"):
#            return print(nom)
#startsWithWove1(name)

noms = ("Aida", "Jordi", "Arnau", "Alex", "Dani")

def startsWithWovel(word):    
    word_lower = word.lower()
    if word_lower.startswith('a'):
        return True 
    if word_lower.startswith('e'):
        return True 
    if word_lower.startswith('i'):
        return True 
    if word_lower.startswith('o'):
        return True 
    if word_lower.startswith('u'):
        return True 
    return False



noms_startsWovel = list(filter(startsWithWovel, noms))

print(list(filter(lambda x: x[0].lower() in 'aeiou', noms)))

print(list(filter(lambda x: (x[0].lower() in 'aeiou')and (len(x)>4), noms)))
