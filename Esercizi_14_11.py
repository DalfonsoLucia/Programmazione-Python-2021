#scrivere una funzione che presi 2 numeri in input li sommi insieme

def somma_numeri():
    a = input("inserisci numero")
    b = input("inserisci numero")
    print(int(a) + int(b))
print("esegui somma numeri")
somma_numeri()

#scrivere una funzione che presi 2 numeri in input e una stringa rappresentante l'operazione da fare (addizione o sottrazione)
def operazione_numeri():
    a = int (input("inserisci numero"))
    b = int (input("inserisci numero"))
    c = input("scegli se vuoi sommare o sottrarre l'operazione")

    #SOLUZIONE 1
    if c == "somma":
        print((a) + (b))
    if c == "sottrazione":
        print((a) - (b))
    if c == "moltiplicazione":
        print((a) * (b))
    if c == "divisione":
        print((a) / (b))

    #SOLUZIONE 2 equivalente alla soluzione 1 ma più efficiente
    if c == "somma":
        print((a) + (b))
    #elif è else if contratto
    elif c == "sottrazione":
        print((a) - (b))
    elif c == "moltiplicazione":
        print((a) / (b))
    else:
        print((a) / (b))


    #if c == "somma":
        #print(int(a) + int(b))
    #else:
     #   if c == "sottrazione":
      #      print(int(a) - int(b)) Questo codice non è molto pulito 

print("esegui operazione numeri")
operazione_numeri()

#scrivere una funzione che presi 3 numeri in input moltipli il secondo con in terzo e aggiuga il primo

def operazione_numeri_1():
    a_1 = int (input("inserisci numero"))
    b_1 = int (input("inserisci numero"))
    c_1 = int (input("inserisci numero"))
    print(b_1 * c_1 + a_1)

print("esegui operazione numeri_1")
operazione_numeri_1()

#scrivere una funzione che presi 3 numeri in input e una stringa rappresentante l'operazione da fare, 
    #moltipli il secondo con in terzo e aggiuga/sottragga il primo

def operazione_numeri_2():
    a_2 = input("inserisci numero")
    b_2 = input("inserisci numero")
    c_2 = input("inserisci numero")
    d_2 = input ("scegli che operazione fare")
    e_2 = int(b_2) * int(c_2)
    if d_2 == "somma":
        print(int(e_2) + int(a_2))
    if d_2 == "sottrazione":
        print(int(e_2) - int(a_2))

print("esegui operazione numeri_2")
operazione_numeri_2()

#scrivere una funzione che presi 3 numeri in input e due stringa rappresentante l'operazione da fare, 
    #la prima sommerà o sottrarrà in base alla scelta dell'utente il primo col secondo numero e la seconda moltiplicherà o dividerà
    #il risultato dato dalla scorsa operazione col terzo numero

def operazione_numeri_3():
    a_3 = input("inserisci numero")
    b_3 = input("inserisci numero")
    c_3 = input("inserisci numero")
    d_3 = input("scegliere se sommare o sottrare il primo numero col secondo")
    e_3 = input("scegliere se moltiplicare o dividere il risultato di f_3 con il terzo numero")
    f_3 = 0
    g_3 = 0
    if d_3 == "somma":
        f_3 = (int(a_3) + int(b_3))
    if d_3 == "sottrazione":
        f_3 = (int(a_3) - int(b_3))
    if e_3 == "moltiplicazione":
        g_3 = (int(f_3) * int(c_3))
    if e_3 == "divisione":
        g_3 = (int(f_3) / int(c_3))
    print(g_3)

print("esegui operazione numeri_3")
operazione_numeri_3()

    
    
    
