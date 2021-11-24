#vogliamo un programma che stampi 10 volte nel terminale una stringa inserita dall'utente. realizzare:
#diagramma di flusso
#pseudocodice
#implementazione Python

# def stampa():
#     s = str(input("inserisci stringa"))
#     contatore = 0
#     while contatore < 10:
#         print(s)
#         contatore = contatore +1

# stampa()

#Vogliamo che la stampa a terminale del nome utente sia solo se l'indice del ciclo è maggiore di 5.
#diagramma di flusso
#pseudocodice
#implementazione Python

# def stampa_1():
#     s = str(input("inserisci nome utente"))
#     contatore = 0

#     while contatore < 10:
#         if contatore > 5:
#             print(s)
#         else:
#             ("Vai oltre!")

#         contatore = contatore +1


# stampa_1()

#in input numero A e B e stampa il maggiore. STAMPI A
#diagramma di flusso
#pseudocodice
#implementazione Python

# def stampa_maggiore():
#     a = int(input("num1"))
#     b = int(input("num2"))
#     if a >= b:
#         print("sono in a > b")
#         print(a)
#     elif a < b:
#         print("sono in b > a")
#         print(b)
#     else:
#         print("sono pari")

# stampa_maggiore()

#dato un numero n preso in input, stampare i numeri che vanno da 1 ad n ma solo se sono pari.
#suggerimento:(contatore%2==0)
#diagramma di flusso
#pseudocodice
#implementazione Python

def stampaPari():
    n = int(input("inserisci numero"))
    contatore = 1
    while (contatore < n):
        if(contatore % 2==0 ):
            print(contatore)
        contatore = contatore +1

stampaPari()
        
def stampaPari():
    n = int(input("inserisci numero"))
    for i in range (1 + n+1):
        if(i % 2 == 1 or i % 2 > 0):
            print(i)

stampaPari()

# function isPari(n):
#     return

