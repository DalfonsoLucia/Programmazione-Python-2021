# Esercizio 004: Sei una Vocale?
# Scrivi una funzione a cui viene passato un carattere come parametro, 
# se ne vengono inseriti più di un carattere inserisci messaggio di errore
# e che ci dice se il carattere è o meno una vocale.

def cercavocale(x):
    if len(x) != 1:
        print("ERROR")
    elif x in "aeiou":
        print("il carattere è una vocale")
    else:
        print("il carattere non è una vocale")
    

# OPPURE

def cerca_vocali(carattere):
    vocali = "aeiou"
    if len(carattere) != 1:
        print("ERROR")
    elif carattere in vocali:
        print(f"Il carattere {carattere} è una vocale")
    else:
        print(f"Il carattere {carattere} non è una vocale")

# I METODI VENGONO MESSI SEMPRE ALLA FINE DEL PROGETTO

x = input("inserisci carattere")
cercavocale(x)
cerca_vocali(x)