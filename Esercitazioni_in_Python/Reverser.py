# Esercizio 007: Reverser
# Scrivi una funzione a cui passerai come parametro una stringa, 
# e che manderà in print una versione inversa (al contrario) della stessa stringa (ad esempio "abcd" diventerà "dcba")

def reserver(stringa):
    result = ""
    for val in stringa:
        result = val + result
    return(result)


#PER QUESTO ESERCIZIO VI SONO ALTRI 2 POSSIBILI SOLUZIONI

def reserver2(stringa):
    cont = len(stringa) -1
    result = ""
    while cont >= 0:
        result += stringa[cont]
        cont = cont -1
    return(result)

#OPPURE

def reverser_pro(stringa):
    reverse = stringa[::-1]
    return(reverse)

stringa = input("inserisci stringa")
print(reserver(stringa))
print(reserver2(stringa))
print(reverser_pro(stringa))