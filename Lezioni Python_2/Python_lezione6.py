#scrivere una funzione che stampi la prima parte del codice fiscale
#fermarsi al mese di nascita

# def codicefiscale():
#     cognome = input("cognome")
#     nome = input("nome")
#     # anno = input("anno di nascita")
#     # annoInStringa = int(anno)
#     # mese = input("inserisci mese")
#     consonante = ""
#     for lettera in cognome:
#         if not (lettera == "a" or lettera == "e" or lettera == "i" or lettera == "o" or lettera == "u"):
#             consonante = consonante + lettera
#             lettera_2 = consonante[0:3].upper()
#     print(lettera_2)
#     nome1 = ""
#     for lettera in nome:
#         if not (lettera == "a" or lettera == "e" or lettera == "i" or lettera == "o" or lettera == "u"):
#             nome1 = nome1 + lettera
#             if len(nome) < 2 :
#                 nome

                
    

           

# codicefiscale()

cognome = input("cognome")
nome = input("nome")
anno = input("anno di nascita")
annoInStringa = int(anno)
m = mese = input("inserisci mese")

nome = nome.lower()
cognome = cognome.lower()


def prendiconsonanti (s):
    numero_caratteri = 0
    risultato = ""
    for lettera in s:
        if lettera not in "aeiou" and numero_caratteri <= 3:
            risultato = risultato + lettera
            numero_caratteri = numero_caratteri + 1

    return risultato

def calcolamese(m):
    if(m == "gennaio"):
        return "A"
    if(m == "febbraio"):
        return "B"
    if(m == "marzo"):
        return "C"
    if(m == "aprile"):
        return "D"
    if(m == "maggio"):
        return "E"
    if(m == "giugno"):
        return "H"
    if(m == "luglio"):
        return "L"
    if(m == "agosto"):
        return "M"
    if(m == "settembre"):
        return "N"
    if(m == "ottobre"):
        return "O"
    if(m == "novembre"):
        return "P"
    if(m == "dicembre"):
        return "Q"

codicefiscale = prendiconsonanti(cognome)
codicefiscale = codicefiscale + prendiconsonanti(nome)
codicefiscale = codicefiscale + anno[2:4]
codicefiscale = codicefiscale + calcolamese(mese)

print(codicefiscale)