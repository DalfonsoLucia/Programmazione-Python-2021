# Esercizio 005: Sommatrice Inarrestabile
# Scrivi una funzione "sommatrice" che somma tra loro tutti gli elementi di una lista di numeri.

def somma_in_lista():
    somlista = []
    l = int(input("inserisci lunghezza lista"))
    for i in range(0, l):
        el = int(input("inserisci numeri in lista"))
        somlista.append(el)
    somma = sum(somlista)
    print(somma)

# OPPURE

def sommatrice(lista):
    risultato = 0
    for numero in lista:
        risultato += numero
    print("Il risultato della somma è... " + str(risultato))

# LA def crealista VA A IMPLEMENTARE LA FUNZIONE def sommatrice

def crealista():
    lista2 = []
    l3 = int(input("inserisci lunghezza lista"))
    for i in range(0, l3):
        al = int(input("inserisci numero"))
        lista2.append(al)
    return lista2

# LA CHIAMATA DEI METODI VIENE MESSA ALLA FINE DEL PROGETTO

somma_in_lista()
listagenerata = crealista()
sommatrice(listagenerata)