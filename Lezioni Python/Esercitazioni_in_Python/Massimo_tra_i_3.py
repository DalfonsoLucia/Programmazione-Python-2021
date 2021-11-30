# Esercizio 002: Max tra Tre Numeri
# Scrivi una funzione che prende stavolta tre numeri come parametro e restituisce il più grande tra loro!

def massimotrenumeri():
    a = int(input("inserisci il primo numero"))
    b = int(input("inserisci il secondo numero"))
    c = int(input("inserisci il terzo numero"))
    if a >= b and a >= c:
        print("il numero maggiore è a", str(":"), a)
    elif b >= c and b >= a:
        print("il numero maggiore è b", str(":"), b)
    else: 
        c >= a and c >= b
        print("il numero maggiore è c",str(":"), c)

# SOLUZIONE DAL SITO

def my_max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c

# LA CHIAMATA DEI METODI VIENE MESSA IN FONDO AL PROGETTO

massimotrenumeri()
my_max_of_three()
