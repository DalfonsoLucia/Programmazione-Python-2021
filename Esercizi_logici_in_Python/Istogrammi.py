# Esercizio 010: Generatore di Istogrammi
# Scrivi una funzione che, data una lista di numeri, fornisce in output un istogramma basato su questi numeri, 
# usando asterischi per disegnarlo.

#Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:

#***
#*******
#*********
#*****

def istogrammi(listaisto):
    for val in listaisto:
        result = ""
        for i in range(0, val):
            result += "*"
        print(result)


def istogrammasingolo(numisto):
    result1 = ""
    while numisto > 0:
        result1 += "*"
        numisto = numisto - 1
    return(result1)


def istomarge(isto):
    print("Risultato di isto ")
    for num in isto:
        asterisk = istogrammasingolo(num)
        print(asterisk)


listaisto = [3, 7, 9, 5]
istogrammi(listaisto)
istomarge(listaisto)

        

