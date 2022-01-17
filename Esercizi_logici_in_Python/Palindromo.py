# Esercizio 008: Palindromo... o non Palindromo?
# Scrivi una funzione a cui viene passata una parola e riconosce se si tratta di un palindromo
# (parole che si leggono uguali anche al contrario) oppure meno.

def palindromo(stringa):
    # if len(stringa) % 2 == 0: #SI USA % 2 == 0 PER VEDERE SE LA STRINGA HA UN NUMERO PARI DI CARATTERI AL SUO INTERNO
        tmp = 0 #tmp = 0 PER IMPOSTARLO SU STRINGHE SI CARATTERI PARI
        meta_stringa = int(len(stringa) / 2)
        stringa_first = stringa[:meta_stringa]
        if len(stringa) % 2 == 1: 
            tmp = 1 #tmp è 1 PER STRINGHE DI CARATTERI DISPARI
        stringa_last = stringa[meta_stringa +tmp:] 
        stringa_last = reverser_pro(stringa_last)
        if stringa_first == stringa_last:
            print("la stringa è palindroma", stringa_first, stringa_last)
        else:
            print("la stringa non è palindroma", stringa_first, stringa_last)

def reverser_pro(stringa):
    reverse = stringa[::-1]
    return(reverse)

stringa = input("inserisci stringa")

palindromo(stringa)
