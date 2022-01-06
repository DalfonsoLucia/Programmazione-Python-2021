
# Fare un programma che inserisca dei numeri il computer ma in modo random

import random

# GENERA UNA LISTA RANDOM DI NUMERI DOVE IL LORO NUMERO TOTALE E IL NUMERO MASSIMO SONO DECISI DALL'UTENTE
def generaListaRandom():
    lista = []
    n = int(input("inserisci numeri da generare casaulamente"))
    n2 = int(input("inserisci range massimo numeri random"))
    for i in range (0,n):
        casuale = random.randrange(1,n2)
        lista.append(casuale)
    return(lista)

        # presa una lista in input stampa il suo contenuto

def stampalista(lista2):
        print(lista2)

lista2 = generaListaRandom()
stampalista(lista2)
