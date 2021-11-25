#voglio un programma che stampi 10 volte mel terminale una stringa inserita dall'utente.

# def stampa():
    # s = str(input("inserisci stringa"))
    # contatore = 0
    # while contatore < 10:
    #     print(s)
    #     contatore = contatore +1

    
    # s = str(input("inserisci stringa"))
    # conta_fino_a = 10

    # for a in range(0, conta_fino_a):
    #     print(a)

    # stampa()

#STRINGHE

# stringa_da_attraversare = "lucia"

# contatore = 0
# while(contatore < len(stringa_da_attraversare)):
#     carattere = stringa_da_attraversare[contatore]

#     print(carattere)
#     contatore = contatore +1

# for lettera in stringa_da_attraversare:
#     print(lettera)

# frutto = "banana"
# for lettera in frutto:
#     print(lettera)

# s = "Monty Python"
# s[0:5]
# print(s[0:5])
# #si stampa così per prende solo alcuni caratteri,di cui dalla posizione 0 alla posizione del carattere 5 e quindi verrà fuori solo Monty.
# print(s[6:12])
# print(s[:7])
# print(s[7:])
# print(s[:]) #così dice dammi tutta la stringa

# saluto = "Ciao Mondo!"
# nuovo_saluto = "M" + saluto[1:5]
# print(nuovo_saluto)

# def trova(parola, lettera):
#     parola = "parola utente"
#     lettera = " "
#     indice = 0
#     indice_lettera_trovata= - 1

#     while indice < len(parola):
#         if parola[indice] == lettera:
#             indice_lettera_trovata = indice
#     indice = indice + 1
    

# print(indice_lettera_trovata)

#scrivere un programma che calcola la lunghezza di una stringa di input
#es. input: "davide"
#output: 6

# def lunghezza_stringa_nome():
#     stringa = input("inserisci stringa")
#     print(len(stringa))

# lunghezza_stringa_nome()

# def lunghezza_stringa_nome():

#     s = input("inserisci stringa da contare")
#     contatore = 0
#     lunghezza_stringa_nome = 0
#     while contatore < len(s):
#             lunghezza_stringa_nome = lunghezza_stringa_nome + 1
#             contatore = contatore + 1

#     print(lunghezza_stringa_nome)

# lunghezza_stringa_nome()

# s = input("inserisci stringa da contare")
# lunghezza_stringa_nome = 0
# for i in s:
#     lunghezza_stringa_nome = lunghezza_stringa_nome + 1
        

# print(lunghezza_stringa_nome)

#scrivi una funzione Python per ottenere una stringa composta 
#da 4 copie degli ultimi due caratteri di una stringa specificata (la lunghezza deve essere almeno 2)
#"Python" -> onononon

# def ripeti_stringa():
#     s = input("inserisci stringa")
#     porzione_stringa = s[-2:]
#     print(porzione_stringa + porzione_stringa + porzione_stringa + porzione_stringa)

# ripeti_stringa()

def prendi_input():
    s = input("inserisci stringa ")
    while(len(s) < 2):
            s = input("inserisci stringa")

    # for i in range(0, len(s)):
    #     ns = ns + s[-2] + s[-1]
    print(s[len(s)-2:] * 4)
        
prendi_input()











