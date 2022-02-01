# scrivi una funzione func che calcola la radice quadrata di un numero positivo
# suggerimento: utilizza il modulo math della libreria standard (cerca la funzione sqrt)

from math import sqrt

def func(numero):
    try:
        return sqrt(numero)
    except ValueError as e:
        print(f"Devi inserire un numero positivo: {e}") 

print(func(9))


            
