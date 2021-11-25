#calcolare la somma di tutti i numeri da 1 al numero dato in input
# esempio, se digito 10 la somma sarà 55
#10 + 8 + 7...
#se digito 3 la somma sarà 7

# assegna variabile risultato
# for i in range(1,n):
#   risultato = risultato + i
#esempi di codice da dove prendere spunto
#per assegnazione variabile
#if operazione == "addizione"
#       risultato = num1 + num2

#Per il loop da contoallarovescia

def stampa_somma():
    numero = int(input("Inserisci numero da sommare"))
    risultato = 0
    
    for i in range(1, numero + 1):
        risultato =  risultato + i
    print(risultato)

stampa_somma()

# #calcolare il prodotto di tutti i numeri da 1 al numero dato in input
# esempio, se digito 10 la somma sarà 55
#10 + 8 + 7...
#se digito 3 il prodotto sarà 7

# assegna variabile risultato
# for i in range(1,n):
#   risultato = risultato + i
#esempi di codice da dove prendere spunto
#per assegnazione variabile
#if operazione == "moltiplicazione"
#       risultato = num1 + num2

#Per il loop da contoallarovescia

def prodotto_numeri():
    risultato = 1
    numero = int(input ("inserisci il numero da moltiplicare")) 
    

    for i in range(1, numero + 1):
         risultato =  risultato * i
    print("la moltiplicazione totale è:" , risultato)
     
    n = 10
    while (i<=prodotto_numeri):
        prodotto_numeri = prodotto_numeri * 1
    i = i + 1


prodotto_numeri()
 
#scrivere un programma per stampare la relativa tabella di moltiplicazione del 2.
#l'output che vogliamo sarà, 2,4,6,8,...


def tabella_numeri():
    n = int(input ("inserire il numero da moltiplicare"))

    n = 2

    for i in range(1, 11):
        prodotto = n * i
        print("la tabella è..." , prodotto)

tabella_numeri()
 