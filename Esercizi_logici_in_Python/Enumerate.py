# Scrivi una funzione func che accetta una lista e stampa ogni elemento della lista eccetto quello a indice 1
#func(["ciao", 1, 50, "A"]):
# l'output dovrà essere:
# ciao
# 50
# "A"

def func(lista):
    for i,item in enumerate(lista):
        if i == 1:
            continue
        else:
            print(item)

func(["ciao", 1, 50, "A"])

