# Esercizio 011: A ciascuno il suo
# Scrivi una funzione che data in ingresso una lista A contenente n parole,
# restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.

def func(listaA):
    listaB = []
    for el in listaA:
        listaB.append(len(el))
    return(listaB)

print(func("Ciao mi chiamo Lucia"))

# OPPURE SI PUò SCRIVERE:

def char_counter_pro(listaA):
    return [len(el) for el in listaA]

print(func("Ciao mi chiamo Lucia"))