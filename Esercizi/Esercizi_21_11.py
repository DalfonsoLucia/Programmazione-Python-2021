
def costruiscinominativoconsonante(s):
    result = ""
    numerocaratteri = 0
    

    # for lettera in s:                     #ti scorre l'array e mette già gli elementi per indice
    #     if lettera not in "aeiou":
    #         result = result + lettera
    #     result_2 = result.upper()
    # return(result_2)

    while numerocaratteri < len(s):             # a differenza del fro qui devi aggiornare tu il valore di ogni singolo elemento in questo caso lettera 
        lettera = s[numerocaratteri]            # e il suo contatore.
        if lettera not in "aeiou":
            result = result + lettera
            result_2 = result.upper()

        numerocaratteri = numerocaratteri + 1
    return(result_2)
    



# costruiscinominativoconsonante("giovanni")

nome = input("inserisci nome")
cognome = input("inserisci cognome")

nomeconsonanti = costruiscinominativoconsonante(nome)
cognomeconsonante = costruiscinominativoconsonante(cognome)

print(nomeconsonanti [0:3] + cognomeconsonante [0:3])

# for lettera in s: 
#         if lettera not in "aeiou " and numero_caratteri <=3: 
#             risultato = risultato + lettera
#             numero_caratteri = numero_caratteri + 1

# numero_caratteri = 0
# for lettera in s:
#         if lettera not in "aeiou":
#             if numero_caratteri <=3:
#                 risultato = risultato + lettera
#                 numero_caratteri = numero_caratteri + 1


# def say_hello(name='one', name2 = "two"):
#     print(name)
#     print(name2)

# say_hello()