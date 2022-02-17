# ESERCIZIO
# 1) Scrivere una classe che rappresenta i quaderni 
# e che contiene informazioni sul numero di pagine
# e il colore del quaderno

# 2) Scrivere un metodo della classe dei quaderni per 
# cambiare il colore del quaderno

# 3) Scrivere un metodo della classe dei quaderni che
# chiede all'utente un numero e lo imposta sull'oggetto


class Notebook:
    def __init__ (self, pages, color):
        self.pages = pages
        self.color = color

    def change_color(self, col): #dentro una classe def è un metodo e non più una funzione
        self.color = col



notebook1 = Notebook(500, "red")
notebook1.change_color("black")


print("Il numero di pagine è " + str(notebook1.pages))
print("Il colore del quaderno è " + str(notebook1.color))


num = input("inserisci numero")
print(num)



