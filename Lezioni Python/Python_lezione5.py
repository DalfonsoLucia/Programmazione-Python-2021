#Scrivere un programma che data una stringa in input, la stampi prima tutta in uppercase e successivamente in lowercase.

# stringa = input(" inserisci stringa")
# print(stringa.upper())
# print(stringa.lower())
# print((stringa.upper()) + " " + (stringa.lower()) + " " + (stringa[0].upper()) + (stringa[1:].lower()))

# contatore = 0
# while (contatore < len(stringa)):
#     print(stringa[contatore].upper)
#     print(stringa[contatore].lower)

#     contatore += 1

# for i in range(0, len(stringa)):
#     print(stringa[i].upper())

# for lettera in stringa:
#     print(lettera.upper())



#metti in uppercase se è pari e in lowercase se è dispari

# s = input("inserisci stringa")
# result = ""
# contatore = 0

# while(contatore < len(s)):
#     c = s[contatore]

#     if(contatore % 2 == 0):
#         result = result + c.upper() #per stampare tutto su una sola riga
#         # print(c.upper())

#     else:
#         result = result + c.lower()
#         # print(c.lower())


#     contatore = contatore +1

# print(result)



# s = input("inserisci stringa")

# contatore = 0

# for carattere in s:
#     if (contatore % 2 == 0):
#         print(s[contatore].upper())
#     else:
#         contatore % 2 != 0
#         print(s[contatore].lower())

#     contatore = contatore +1
    

# def is_even(n):
#     if n%2 == 0:
#         return True
#     else:
#         return False


# print("Prima di pari")
# is_numero_pari = is_even(10)
# print(is_numero_pari)
    
# s = input("inserisci stringa")
# contatore = 0

# for carattere in s:
#     if is_even(contatore):
#         print(s[contatore].upper())
#     else:
#         contatore % 2 != 0
#         print(s[contatore].lower())


#     contatore = contatore +1

#Scrivere un programma che ritorna true o false, true se la lunghezza della stringa è multiplo di 4


# def multiplo_di_4(x):

#     if (x % 4 == 0):
#         return True
#     else:
#         return False

# s = input("inserisci")
# i = 0

# for l in s:
#     i = i +1
# print(multiplo_di_4(i))

# scrivere una funzione Python che stampi (arrotondando in maniera opportuna) 
# al massimo fino ai primi 2 numeri dopo la virgola di un numero decimale.
# suggerimento {:.2f}

def arrotondare():
    num = input ("inserisci numero")
    NumInstringa = float(num)

    result = round(NumInstringa, 2)
    print(result)

    result_2 = "{:.2f}".format(NumInstringa)
    print(result_2)
    if NumInstringa > 3:
        result_3 = round(result, 1)

        NumInstringa_2 = float(result_2)
        result_4 = round(NumInstringa_2, 1)
        
        print(result_3, result_4)

    #print("{:.2f}".format(NumInstringa))


arrotondare()

#Scrivere un programma Python per stampare i seguenti numeri interi 
# con zeri a sinistra della lunghezza specificata.

# num_2 = input("inserisci stringa")
# numeri_di_zeri = ""
# numeriInStringa = str(num_2)


# for i in range(0, len(numeriInStringa)):
#     numeri_di_zeri = numeri_di_zeri + "0"

# print(numeri_di_zeri + numeriInStringa)



# contatore = 0
# while (contatore < i):
#     numeri_di_zeri = numeri_di_zeri + "0"
#     contatore = contatore + 1

#print(numeri_di_zeri)

# def slicing():
#     frutto = "banana"
#     lettera = frutto[:3]
#     print(lettera)

# slicing()