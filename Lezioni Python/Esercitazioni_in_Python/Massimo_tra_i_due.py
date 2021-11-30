# Esercizio 001: Max tra Due Numeri
# Scrivi una funzione che prende due numeri come parametro e manda in print 
# il più grande tra i due.
# Per quanto Python disponga di una funzione max(), sei invitato a utilizzare le istruzioni If, Elif ed Else 
# per la scrittura dell'algoritmo.

def massimoduenumeri():
    a = int(input("inserisci il primo numero"))
    b = int(input("inserisci il secondo numero"))
    if a >= b:
        print("Il numero più grande tra i due è: ", a)
    else:
        b >= a
        print("Il numero più grande tra i due è: ", b)
   
# OPPURE

def my_max(a, b):
    if a == b:
        print("I numeri sono identici")
    elif a > b:
        print("Il numero più grande tra i due è " + str(a))
    else:
        print("Il numero più grande tra i due è " + str(b))

# LA CHIAMATA DEI METODI VIENE MESSA IN FONDO AL PROGETTO

massimoduenumeri()

a2 = int(input("inserisci primo numero"))
b2 = int(input("inserisci secondo numero"))
my_max(a2, b2)