# Esercizio 003: Il Maggiore tra tutti!
# Scrivi un programma che, passata come parametro una lista di interi, 
# fornisce in output il maggiore tra i numeri contenuti nella lista.


def Maggiore():
    listaInteri = []
    l = int(input("inserisci lunghezza lista"))
    
    for i in range(0, l):
        al = int(input("inserisci numero"))
        listaInteri.append(al)
    l2 = max(listaInteri)
    print("il numero più grande è:" + l2)

# OPPURE SI PUO' FARE;

def max_in_list(list):
    my_max = 0
    for num in list:
        if num > my_max:
            my_max = num
    print(f"Il numero più grande della lista passata è {my_max}")

# O ANCHE...

def crealista():
    lista2 = []
    l3 = int(input("inserisci lunghezza lista"))
    for i in range(0, l3):
        al = int(input("inserisci numero"))
        lista2.append(al)
    return lista2


# LA CHIAMATA DEI METODI VIENE MESSA IN FONDO AL PROGETTO

Maggiore()
list = [1, 2, 6, 8, 4]
max_in_list(list)
listagenerata = crealista()
max_in_list(listagenerata)
