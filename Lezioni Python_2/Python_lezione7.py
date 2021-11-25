#ESERCIZIO 1
# Scrivere una funzione "niente_e" che restituisca false se la parola contiene almeno una "e", True altrimenti
# es. casa --> True
#     niente --> False

# def niente_e(s):
#     for lettera in s:
#         if "e" in lettera:
#             return "false"
#         else:
#             return"true"
        

# parola = input("inserisci stringa")

# result = niente_e(parola)

# print(result)

# soluzione
# def niente_e(parola):
#     for lettera in parola:
#         if lettera == "e":
#             return False
# return True


#ESERCIZIO 2
# Popolare una lista di n elementi con i primi n numeri pari.
# Dopo averli inseriti visualizzare in output i valori memorizzati nella lista e la loro posizione.

# 10
# 0 0 1 2 3 4 6 8 10


# n = int(input("inserisci numero"))
# lista_pari = []

# for i in range(0, n+1):
#     if i % 2 == 0:
#         lista_pari.append(i)
# # print(lista_pari)

# val = 0
# for i in lista_pari:
#     # print(val)
#     val = val + 1

# print("Elemento in posizione" + str(val -1) + ":" + str(lista_pari))

# Prendere in input 10 numeri dal terminale e
# stampare la sommatoria di questa lista
# 0, 1, 1, 0, 0, 10, 2, 20, 0, 1
# 35

# listaDiNumeri = []
# sommaNumeri = 0
# for i in range (0, 10):
#     n = int(input("inserisci numero"))
#     listaDiNumeri.append(n)
#     sommaNumeri += n
# print(listaDiNumeri)
# print(sommaNumeri)

# listaDiNumeri = []
# sommaNumeri = 0
# while len(listaDiNumeri) <= 10:
#     n = int(input("inserisci numero"))
#     listaDiNumeri.append(n)
#     sommaNumeri += n
# print(listaDiNumeri)
# print(sommaNumeri)

#ESERCIZI:


