def operazione_numeri():
    risultato = 0
    a = int (input("inserisci numero"))
    b = int (input("inserisci numero"))
    c = input("scegli se vuoi sommare o sottrarre l'operazione")

    """ #SOLUZIONE 1
    if c == "somma":
        print((a) + (b))
    if c == "sottrazione":
        print((a) - (b))
    if c == "moltiplicazione":
        print((a) * (b))
    if c == "divisione":
        print((a) / (b)) """

    #SOLUZIONE 2 equivalente alla soluzione 1 ma più efficiente
    if c == "somma":
        risultato = a + b
    #elif è else if contratto
    elif c == "divisione" and b != 0:
        risultato = a / b
    else:
        risultato = "Inserisci risultato"

    return risultato

nuovoRisultato = operazione_numeri()
print(nuovoRisultato)