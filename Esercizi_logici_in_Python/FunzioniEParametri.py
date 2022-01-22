# Definisci una funzione func che accetta una lista di numeri 
# come parametro e come risultato restituisce la somma dei suoi numeri pari
# quindi func([1,2,3,4,5,6]) deve restituire 12 (2 + 4 + 6)


def func(lista):
    result = 0
    for num in lista:
        if num %2 == 0:
            result += num
    print(result)
    return result 

    
func([1,2,3,4,5,6])


