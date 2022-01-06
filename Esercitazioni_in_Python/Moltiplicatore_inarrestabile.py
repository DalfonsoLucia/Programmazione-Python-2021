# Esercizio 006: Moltiplicatore Inarrestabile
# Scrivi una funzione "moltiplicatrice" che moltiplica tra loro tutti gli elementi di una lista di numeri.

def moltiplicanumeri():
    multinum = []
    l = int(input("inserisci lunghezza lista"))
    for i in range(0, l):
        el = int(input("inserisci numeri in lista"))
        multinum.append(el)

    # DOPO AVER IMPLEMENTATO LA LISTA SI VA A MOLTIPLICARE GLI ELEMENTI IN ESSA CONTENUTI

    prodotto = 1
    for numero in multinum:
        if numero != 0:
            prodotto *= numero
    print("Il risultato della moltiplicazione tra tutti gli elementi della lista è... " + str(prodotto))
    

#OPPURE ED è' PIù PULITO E CHIARO IL CODICE:

def moltiplicatore(lista):
    risultato = 1
    for numero in lista:
        if numero != 0:
            risultato *= numero
    return "Il risultato della moltiplicazione tra tutti gli elementi della lista è..." + str(risultato)


# LA def crealista VA A IMPLEMENTARE LA FUNZIONE def moltiplicatore

def crealista():
    lista2 = []
    l3 = int(input("inserisci lunghezza lista"))
    for i in range(0, l3):
        al = int(input("inserisci numero"))
        lista2.append(al)
    return lista2

# LA CHIAMATA DEI METODI VIENE MESSA ALLA FINE DEL PROGETTO


moltiplicanumeri()
listagenerata = crealista()
print (moltiplicatore(listagenerata))
