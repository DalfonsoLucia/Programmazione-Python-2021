#considera la lista sotto e calcola la somma dei numeri interi presenti al suo interno
# lista = [1, 5, "B", "ciao", 4, (3,4)] -> risultato = 10

lista = [1, 5, "B", "ciao", 4, (3,4)]

risultato = 0
for num in lista:
    if type(num) is int:
        risultato += num
print(risultato)