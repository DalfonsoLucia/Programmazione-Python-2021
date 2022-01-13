#calcola la somma totale dei numeri all'interno della lista sottostante
# lista = [[1,2,3],[4,5]]
# risultato finale = 15

lista = [[1,2,3], [4,5]]

risultato = 0
for el in lista:
    for num in el:
        risultato += num
print(risultato)