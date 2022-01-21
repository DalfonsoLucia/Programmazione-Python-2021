# Dato il dizionario d, scrivi codice che restituisce una lista
# che contiene gli elementi a comune tra le chiavi e i valori
# Devi ottenere ["A", "B"]


d = {
   "A":"B",
   "B":"H",
    "C":"A",
    "D":"Z"}
lista = []

d1 = d.copy()
for k,v in d.items():
    for k1,v1 in d1.items():
        if k == v1:
            lista.append(k)
     
print(lista)

#OPPURE
# usando la dictionary comprehension

[k for k in d.keys() if k in d.values()]

#che il corrispondente è:

l = []
for k in d.keys():
    if k in d.values():
        l.append(k)
print(l)
