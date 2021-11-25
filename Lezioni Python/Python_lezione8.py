# ESERCIZIO N.1
# Date in input due liste di elementi da terminale lunghe n1 e n2, 
# stampare una lista in output che sia la differenza nella prima con la seconda
# es. 4
#     2
#     ["a", "b", "c", "d"]
#     ["a", "b", "f"]
# output ["c", "d"]


# lista1 = []
# lista2 = []

# for i in range(0, 4):
#     n1 = input("inserisci elementi prima lista:")
#     lista1.append(n1)
# print(lista1)

# for i in range(0, 3):
#     n2 = input("inserisci elementi seconda lista:")
#     lista2.append(n2)
# print(lista2)


# difference_1 = set(lista1).difference(set(lista2))   LO RIVEDREMO IN UN SECONDO MOMENTO 
# difference_2 = set(lista2).difference(set(lista1))    PERCHè DOBBIAMO FARE ANCORA I SET

# list_difference = list(difference_2.union(difference_1))
# list_difference.remove("f")
# print(("la differenza è ") , list_difference)

#SECONDA POSSIBILITA'
# l1 = int(input("inserisci lunghezza lista 1: "))
# l2 = int(input("inserisci lunghezza lista 2: "))

# lista1 = []
# lista2 = []
# listaresult = []

# for i in range(0, l1):
#     n1 = input("inserisci elementi prima lista:" + str(i) + ":")
#     lista1.append(n1)

# for i in range(0, l2):
#     n2 = input("inserisci elementi seconda lista:" + str(i) + ":")
#     lista2.append(n2)

# #SOLUZIONE1
# for element_l1 in lista2:
#     while element_l1 in lista1:
#         lista1.remove(element_l1)

# #SOLUZIONE2
# # for element_l1 in lista1:
# #     while element_l1 not in lista2:
# #         listaresult.append(element_l1)



# print(lista1)

# ESERCIZIO N.2
# Scrivi un programma Python per trovare l'elenco di parole più lunghe di n da un determinato elenco di parole.

# parametro n passato in input
# lista di parole invece cablato a codice

# l = int(input("inserisci lunghezza lista"))
# lista = []
# element = ""

# for i in range(0, l):
#     n = input("inserisci elementi:")
#     lista.append(n)
# for element in lista:
#     if len(element) <= l:
#         print(element)


# ESERCIZIO N.3
# Scrivi un programma Python per convertire una lista di caratteri in una stringa

# def convertiListToString():
#     s = ["a", "b", "c", "d"]
#     strl = "".join(s)
#     print(strl)

# ESERCIZIO N.4
#Scrivere un programma Python per aggiungere un elemento preso in input in una tupla
# ES. t = ("a", "b", "c")
#     a = input...

# def aggiungiStringtoTupla():
#     t = ("a", "b", "c")
#     t_1 = "".join(t)
#     s = input("inserisci stringa")
#     s_2 = t_1 + " " + s
#     tuple(s_2)

#     print(s_2)

# def aggiungiStringtoTupla():
#     t = ("a", "b", "c")
#     s = tuple(input("inserisci stringa"))
#     s_2 = t + s

#     print(s_2)

# aggiungiStringtoTupla()

# ESERCIZIO N.5
# Scrivere un programma Python per rimuovere un elemento da una tupla

# def rimuoviElementotupla():
#     t = ("a", "b", "c", "d")
#     t = list(t)
#     t.remove("b")
#     tuple(t)
#     print(t)

# rimuoviElementotupla()

tuplex = ("w", "f" "s" "g")
tuplex  =  tuplex [: 2 ] +  tuplex [ 3 :]
print ( tuplex )


# ESERCIZIO N.6
# Scrivere un programma Python per invertire una tupla di elementi presi in input 
# ES. ("a", "b", "c")
#     ("c", "b", "a")

x = (5,6,7,3)
y = reversed(x)
print(tuple(y))

# oppure 

# print(x[::-1])
