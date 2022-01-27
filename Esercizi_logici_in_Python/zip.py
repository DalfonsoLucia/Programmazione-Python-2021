# Sfruttando zip() devi ottenere il seguente output: [('Roma', 1), ('Milano', 2), ('Napoli', 3)]
# lista = ["Roma", "Milano", "Napoli"]

def func(lista):
    numeri = list(range(1,4))
    print(list(zip(lista,numeri)))

func(["Roma", "Milano", "Napoli"])

