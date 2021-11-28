def main_menù():
    print("benvenuto in agenda, selezionare un menù per continuare")
    print("1) inserisci")
    print("2) elimina")
    print("3) ricerca\n")
    print("4) stampa\n\n")
    print("10) inserisci appuntmento")
    print("11) stampa appuntmento\n\n")
    print("99) esci")

    return int(input("# "))

def inserisci():
    ana = {}
    print("inserisci nuova anagrafica")
    ana(nome = (input("inserisci nome")))
    ana(cognome = (input("inserisci nome")))
    ana(mail = (input("inserisci mail")))
    ana(telefono = (input("inserisci telefono")))
    return ana

def elimina():
    pass

def ricerca():
    pass

def stampa(ana):
    print("nome\tcognome\t\tmail\t\ttelefono")
    for el in ana:
        print(el["nome"] + "\t" + el["cognome"] + "\t\t" + el["mail"] + "\t\t\t" + el["telefono"])


