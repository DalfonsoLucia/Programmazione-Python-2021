# Scrivi un programma Python per estrarre un dato numero di elementi (preso in input) selezionati casualmente da una lista.

# import random

#    ES. lista = ["a", "b", "c", "a", "a"]
# 1 e len(lista)
# 3
# voglio 3 elementi a caso dalla lista

import random
# lista = []
# l = int(input("lunghezza lista"))
# element = int(input("inserisci numeri da prendere"))

# for i in range (1, l):
#     n = input("inserisci elemento")
#     lista.append(n)
# for caratteri in lista:
#      if len(caratteri) <= l:
#          print(caratteri)
        

# print(random.sample(lista, element))

#OPPURE

# def random_select_nums(n_list, n):
#     return  random.sample(n_list, n)

# n_list = [1,4,3,2,4,3,5,6,6]
# selec_nums = 3
# result = random_select_nums(n_list, selec_nums)


# print(result)

# def random_select_nums_with_choise(n_list):
#     print(random.choice(n_list))

# def random_select_nums_with_sample(n_list, n):
#     return  random.sample(n_list, n)

# def random_select_nums_with_randint(n_list, n):
#     for i in range (0, n):
#         random_number = random.randint(0, len(n_list)-1)
    
#     print(random_number)
#     print(n_list[random_number])

# n_list = ["a", "a", "b","f","h","k","t","t"]
# selec_nums = 3
# result_sample = random_select_nums_with_sample(n_list, selec_nums)
# result_choise = random_select_nums_with_randint(n_list, selec_nums)
# random_select_nums_with_choise(n_list)






#############################################
#togli i doppioni degli elementi della lista, usando random e shuffle

# n_list = []
# resultantList = []
# l = int(input("lunghezza lista"))
# elemento = ""

# n_list = ["a", "a", "b","f","h","k","t","t"]
# for element in n_list:
#     if element not in resultantList:
#         resultantList.append(element)


# for i in range (0, l):
#      n = input("inserisci elemento")
#      n_list.append(n)
# for caratteri in n_list:
#     if len(caratteri) <= l:
#         print(caratteri)
# for elemento in n_list:
#     if elemento not in resultantList:
#         resultantList.append(elemento)  


# print(resultantList)

# lista = []
# n = int(input("inserire lunghezza lista"))
# for x in range(0, n):
#     val = input("inserisci valore:")
#     lista.append(val)
# print(lista)

# num = int(input("inserisci il numero di elementi da estrarre casualmente"))
# ls = []
# for x in range(num):
#     a = random.choice(lista)
#     if a not in ls:
#         ls.append(a)
# print(ls)

# ESERCIZIO_2
# Scrivere un programma Python per creare una lista multidimensionale (liste di liste) con zeri.
#   output: [[0,0] [0,0] [0,0]]


def multidimensional():
    n = 2
    lista_esterna = []
    for i in range(0, 3):
        sottolista = []
        for j in range (0, n):
            sottolista.append(0)
            lista_esterna.append(sottolista)

    return lista_esterna

print(multidimensional())


# # SOLUZIONE DAVIDE
# def multidimensional(list_element):
#     nums = []
#     for i in range(3):
#         nums.append([])
#     for j in range (list_element):
#         nums[i].append(0)

#     return nums

# SOLUZIONE DAVIDE CARICATA SU GITHUB
# def multidimensional(list_element):
#     nums = []
#     for i in range(3):
#         nums.append([])
#         for j in range(list_element):
#             nums[i].append(0)

#     return nums

# n = int(input("Quanti elementi per sottolista?")) 
# print(multidimensional(n)) 


# scrivi un programma Python per creare una griglia nXn con numeri
# ES. 3
#       [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# ES. 4
#       [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

def lista_griglia(n):
    griglia = []
    for i in range(n):
        griglia.append ([])
        for j in range (n):
            griglia[i].append(j)

    print(griglia)

lista_griglia(5)


