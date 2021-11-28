# Create un programma che prenda in input una serie di numeri le mette in una lista e poi le ordina, una volta ordinate le stampate
# # senza usare il comando sort

# l = int(input("inserisci lunghezza lista"))
# lista = []
# lista2 = []
# element = ""

# for i in range(0, l):
#     n = int(input("inserisci elementi:"))
#     lista.append(n)
# print(lista)
# print(i + lista.index(n))

# pvar = lista.pop(4)
# lista.insert (0, pvar)
# lista.append(lista.pop(1))

# # COME è VENUTO ALLA FINE E FUNZIONA
# for i in range(0):
#     ls = input("inserisci numero")
#     lista.append(int(ls))
# while len(lista)!= 0:
#     lista2.append(min(lista))
#     lista.remove(min(lista))
# print(lista2)

# COME L'AVEVO FATTO IO ALL'INIZIO E CRASHA
# for i in range(n):
#      if i<= l(lista):
#         lista2.remove(i)
#         lista2.insert(lista)
# else: 
#         lista2.remove(lista)
#         lista2.append(i)
# print(lista)



# n = 0
# l = []
# l2 = []
# for i in range(0):
#     a = input ("inserisci")
#     l.append(int(a))
# while len(l)!= 0:
#   l2.append(min(l))
#   l.remove(min(l))
# print(l2)

# Fare un programma che inserisca dei numeri il computer ma in modo random

import random

def generaListaRandom():
    lista = []
    n = int(input("inserisci numeri da generare casaulamente"))
    n2 = int(input("inserisci range massimo numeri random"))
    for i in range (0,n):
        casuale = random.randrange(1,n2)
        lista.append(casuale)
    return(lista)

# generaListaRandom()

# presa una lista in input stampa il suo contenuto

# lista2 = ["a", "g", "1", "8", "6", "D"]

def stampalista(lista2):
    # for val in lista2:
        print(lista2)

# lista2 = generaListaRandom()
# stampalista(lista2)

