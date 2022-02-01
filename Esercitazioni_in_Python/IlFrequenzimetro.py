# Esercizio 012: Il Frequenzimetro
# Scrivi una funzione a cui passare una stringa come parametro, 
# e che restituisca un dizionario rappresentante la "frequenza di comparsa" 
# di ciscun carattere componente la stringa.


def frequenzimetro(parola):
    d = {}
    for carattere in parola:
        if carattere in d:
            d[carattere] += 1
        else:
            d[carattere] = 1
    return d

print(frequenzimetro("ababcc"))