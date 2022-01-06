import json
# import pyfiglet
# from pyfiglet import figlet_format
# from termcolor import colored
import os

def inserisci():
    ana = {}
    ana['nome'] = input('Nome: ')
    ana['cognome'] = input('Cognome: ')
    ana['email'] = input('Email: ')
    ana['telefono'] = input('Telefono: ')
    listaJson = read_data()
    if len(listaJson) == 0:
        listaJson = {"nominativo" : []}
    listaJson['nominativo'].append(ana)
    save_data(listaJson)

def stampa():
    listaJson = read_data()
    if len(listaJson) == 0:
        return []
    lista = listaJson['nominativo']
    count = 0
    for el in lista:
        print(str(count),str(el))
        count += 1
    input("\n\nPress key to continue")
    return lista

def modifica():
    listaJson = read_data()
    if len(listaJson) == 0:
        return []
    ana = listaJson['nominativo']
    count = 0

  
    for el in ana:
        print(str(count),str(el))
        count += 1
    n = int(input("\n\nIndica il contatto da modificare"))
    if n > len(ana) -1:
        return []
    nominativo = ana[n]
    nominativo['nome'] = input('Nome: ')
    nominativo['cognome'] = input('Cognome: ')
    nominativo['email'] = input('Email: ')        
    nominativo['telefono'] = input('telefono: ')        
    
    print(ana)
    save_data(listaJson)


def cancella():
    lst = stampa()
    id_del = int(input("Inserisci ID da cancellare: "))
    del(lst[id_del])
    save_data(lst)
    return True

def main_screen():
    # result = pyfiglet.figlet_format("Agenda", font="slant")
    #print(colored(result,"red"))
    print("agenda")

def save_data(dt):
    fp = open('agenda.dat', 'w')
    fp.write(json.dumps(dt))
    fp.close()

def read_data():
    fp = open('agenda.dat', 'r')
    dati_agenda = fp.read()
    fp.close()
    agenda = json.loads(dati_agenda)
    return agenda


def clear_dbfile():
    fp = open('agenda.dat', 'w')
    fp.write('[]')
    fp.close()

# menu gestione programma

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    main_screen()
    print("\n")
    print("1. Inserisci")
    print("2. Stampa")
    print("3. Modifica\n\n")
    print("10. Elimina\n\n")
    print("11. Purge DB\n")
    print("99. Esci\n\n")

    cmd = input("#: ")
    if(cmd == '99'):
        exit()
    elif(cmd=='1'):
        inserisci()
    elif (cmd == '2'):
        stampa()
    elif (cmd == '3'):
        modifica()
    elif (cmd == '10'):
        cancella()
    elif (cmd == '11'):
        clear_dbfile()
    else:
        print("comando inserito: " + cmd)
    return True

