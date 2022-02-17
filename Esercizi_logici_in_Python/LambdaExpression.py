# Scrivi una funzione func che riceve due parametri:
# - una lista di stringhe 
# - una lettera
# la funzione deve restituire una lista contenente solo quelle stringhe che contengono la lettera
# func( ["ciao", "Andrea", "Luigi", "Marco"], "i") -- > ["ciao", "Luigi"]
# Non usare list comprehension

def func(lista, lettera):
    l = []
    #for stringa in lista:
    #    if lettera in stringa:
    #        l.append(stringa)
    esempioLamda(lista, lettera, l)
    print(l)

def esempioLamda(lista, lettera, l):
    for stringa in lista:
        if lettera in stringa:
            l.append(stringa)

func(["ciao", "Andrea", "Luigi", "Marco"], "i")

# L'EQUIVALENTE CON LE LAMBDA EXPRESSION è:  

def func(lista, lettera):
    print(list(filter(lambda stringa: lettera in stringa , lista)))

func(["ciao", "Andrea", "Luigi", "Marco"], "i")

#   QUI DI SEGUITO VEDREMO IL NOME PIù LUNGO E IL PIù CORTO USANDO LE FUNZIONI min E max E LA FUNZIONE KEY

lista = ["Andrea","Marco","Ida","Francesco"]

print(max(lista, key = lambda nome: len(nome)))
print(min(lista, key = lambda nome: len(nome)))

#COME POSSIAMO VEDERE COME SI USANO LE LAMBDA EXPRESSION.