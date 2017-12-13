dices = [1, 2, 3, 4, 5, 6]
players = []
listarandom = []
elegidos = []
player1 = []
player2 = []

import random


def pintardados(dados):
    d1 = "  .-------."
    d2 = " /       /|"
    d3 = "/_______/ |"
    # d4 = "| o   o | |"
    # d5 = "| o o o | /"
    # d6 = "| o   o |/ "
    d7 = "'-------'  "

    print multidado(d1, dados)
    print multidado(d2, dados)
    print multidado(d3, dados)
    print multidadov(dados, 1)
    print multidadov(dados, 2)
    print multidadov(dados, 3)
    print multidado(d7, dados)


def multidado(lin, dados):
    v = ""
    for i in range(len(dados)):
        v = v + "       " + lin
    return v


def multidadov(dados, linea):
    dvini = "| "
    v = "       "
    for i in range(len(dados)):
        v = v + dvini
        if (linea == 1):
            if (dados[i] == 4 or dados[i] == 5 or dados[i] == 6):
                v = v + "o   "
            else:
                v = v + "    "
            if (dados[i] == 2 or dados[i] == 3 or dados[i] == 4 or dados[i] == 5 or dados[i] == 6):
                v = v + "o "
            else:
                v = v + "  "
            v = v + "| |"
        if (linea == 2):
            if (dados[i] == 6):
                v = v + "o "
            else:
                v = v + "  "
            if (dados[i] == 1 or dados[i] == 3 or dados[i] == 5):
                v = v + "o "
            else:
                v = v + "  "
            if (dados[i] == 6):
                v = v + "o "
            else:
                v = v + "  "
            v = v + "| /"
        if (linea == 3):
            if (dados[i] == 2 or dados[i] == 3 or dados[i] == 4 or dados[i] == 5 or dados[i] == 6):
                v = v + "o   "
            else:
                v = v + "    "
            if (dados[i] == 4 or dados[i] == 5 or dados[i] == 6):
                v = v + "o "
            else:
                v = v + "  "
            v = v + "|/ "
        v = v + "       "
    return v


"""def barajar(num_veces,dices):
    lista=[]
    for i in range (num_veces):
        dado=random.choice(dices)
        lista.append(dado)
        pintardados(dado)
    return lista"""


def barajar(num_veces, dices):
    lista = []
    for i in range(num_veces):
        lista.append(random.choice(dices))
    return lista


def elegirdados(elegidos, listarandom):
    pintardados(listarandom)
    print "------------------"
    print listarandom
    print "------------------"
    chose = input("Write the number of each dice you want to keep. To stop press 0:  ")

    while chose != 0:
        elegidos.append(chose)
        if chose in listarandom:
            listarandom.remove(chose)
        chose = input("Which one else: ")


def tirada(dices, listarandom, elegidos):
    listarandom = barajar(5, dices)

    elegirdados(elegidos, listarandom)

    for i in range(len(listarandom)):
        listarandom = barajar(5 - len(elegidos), dices)

    elegirdados(elegidos, listarandom)

    print "Last roll:"

    for i in range(len(listarandom)):
        listarandom = barajar(5 - len(elegidos), dices)

    pintardados(listarandom)
    
    print "------------------"
    print listarandom
    print "------------------"
    chose = input("Write the ones that left. To stop press 0: ")

    while chose != 0:
        elegidos.append(chose)
        if chose in listarandom:
            listarandom.remove(chose)
        chose = input("Which one else: ")

    return elegidos


# funcion juego#

def juego():
    print "======================================================"
    name1 = raw_input("Player 1 > Please, insert your nickname: ")
    player1.append(name1)
    name2 = raw_input("Ok! Now Player 2 > ")
    player2.append(name2)
    print "======================================================"

    print "==============================================================================================================================="
    print "Ok, ", name1, "you have to roll three times and pick from your dices which ones you want to keep." \
                         " Try to choose the highest combination in order to get the maximum score. "
    print "==============================================================================================================================="

    print "First roll: "

    tirada(dices, listarandom, elegidos)

    suma1 = 0
    for i in elegidos:
        suma1 = suma1 + i
        player1.append(suma1)

    print "================================="
    print name1, ", your score is: ", suma1
    print "================================="

    players.append(name1)
    players.append(player1[5])

    del listarandom[:]
    del elegidos[:]

    print "==============================================================================================================================="
    print "Well, ", name2, ". Now is your turn. Remember to choose the highest ones."
    print "==============================================================================================================================="
    print "First roll: "

    tirada(dices, listarandom, elegidos)

    suma2 = 0
    for i in elegidos:
        suma2 = suma2 + i
        player2.append(suma2)

    print "================================"
    print name2, ", your score is: ", suma2
    print "================================"

    print "Scores: ", name1, player1[5], name2, player2[5]

    players.append(name2)
    players.append(player2[5])

    del listarandom[:]
    del elegidos[:]

    print "************************************************"
    if suma1 > suma2:
        print "Winner is ", name1, ". Congrats! "
    elif suma1 < suma2:
        print "Winner is ", name2, ". Congrats!"
    else:
        print "Draw"


def menu():
    print " ------------------------- "
    print "| Y A H T Z E E   L I T E |"
    print " ------------------------- "
    print "| 1) Play                 |"
    print "| 2) Scores               |"
    print "| 3) Exit                 |"
    print " ------------------------- "


# juego#
opcion = 0
while opcion != 3:
    menu()
    opcion = input("Choose option: ")
    if opcion == 1:
        juego()
    elif opcion == 2:
        print players

