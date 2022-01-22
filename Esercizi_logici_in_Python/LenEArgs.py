# Definsici una funzione func
# che può ricevere un numero arbitrario di positional arguments 
# e per ogni argomento la funzione deve stampare la sua lunghezza (len)
# passa come argomenti solo delle stringhe

def func(*args):
    for el in args:
        print(len(el))

func("Lucy in the sky with diamonds")

print("Variazione esercizio - numero misto di *args")

# e se la nostra func avesse un numero misto di positional arguments?


def func(*args):
    for el in args:
        if type(el) != str:
            el = str(el)
        print(len(el))
        

func("Lucy in the sky with diamonds", "Beatles", 1967)

