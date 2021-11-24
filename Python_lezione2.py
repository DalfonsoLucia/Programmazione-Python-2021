#def contoallarovescia(n):
    #while n > 0:
     #   print(n)
      #  n = n -1



#for i in range(1,5):
 #   print(i)

#contoallarovescia(3)

#scrivere una funzione che stampa n volte il vostro nome preso in input (nelle parentesi) usate sia modalità for che while

def stampa_nome(nome):
    n=11
    #for i in range(1,n):
     #   print(nome)

    
    while n > 0:
        print(str(n) + ". " + nome)
        n = n -1


stampa_nome("Lucia")


#scrivere una funzione che ad ogni iterazione stampa il num inserito dall'utente aggiungendo + 2

def contoallarovescia():
    n = 10
    while n > 0:
        print(n)
        n = n -1

    for i in range(1, n):
        print("fine conto")
        


contoallarovescia()