import os
from classicLotoData import *
def ClearSystem():
    os.system('cls')
def MenuLotoClassic():
    userInput = input("\nMenu :\n1- Obtenir les numéros préférables à jouer\n2- Obtenir plus d'informations\n3- Obtenir les derniers resultats\n4- Revenir au menu principal\n> ")
    if userInput == "1":
        ClearSystem()
        LotoClassic()
    elif userInput == "2":
        ClearSystem()
        LotoClassicMoreResults()
    elif userInput == "3":
        ClearSystem()
        LotoClassicLastResults()
    elif userInput == "4":
        ClearSystem()
        main()
    else:
        ClearSystem()
        print("*****************\nChoix incorrect !\n*****************")
def LotoClassic():
    print("**************************************\nRatiaux des 5 boules les plus tirées :\n**************************************\n")
    finalResultClassic = sorted(finalNumberClassicDico.items(), key=lambda x: x[1], reverse = True)
    a = 0
    while a<5:
        for i in finalResultClassic:
            print(i[0], i[1])
            a += 1
            if a == 5:
                break
    print("\n******************************************\nRatiaux de la boule chance la plus tirée :\n******************************************\n")
    finalResultChance = sorted(finalNumberChanceDico.items(), key= lambda x: x[ 1 ], reverse= True )
    b = 0
    while b<1:
        for i in finalResultChance:
            print(i[0], i[1])
            b += 1
            if b == 1:
                break
    userInput = input("\nMenu :\n1- Revenir au menu loto classique\n2- Revenir au menu principal\n3- Quitter l'application\n> ")
    if userInput == "1":
        ClearSystem()
        MenuLotoClassic()
    elif userInput == "2":
        ClearSystem()
        main()
    elif userInput == "3":
        quit()
    else:
        ClearSystem()
        print("*****************\nChoix incorrect !\n*****************")
def LotoClassicMoreResults():
    print("**************************************\nBoules les plus tirées :\n**************************************\n")
    finalResultClassic = sorted(finalNumberClassicDico.items(), key=lambda x: x[1], reverse = True)
    a = 0
    while a<5:
        for i in finalResultClassic:
            print(i[0], i[1])
            a += 1
    print("\n******************************************\nBoules chances tirées :\n******************************************\n")
    finalResultChance = sorted(finalNumberChanceDico.items(), key= lambda x: x[ 1 ], reverse= True )
    b = 0
    while b<1:
        for i in finalResultChance:
            print(i[0], i[1])
            b += 1
    userInput = input("\nMenu :\n1- Revenir au menu loto classique\n2- Revenir au menu principal\n3- Quitter l'application\n> ")
    if userInput == "1":
        ClearSystem()
        MenuLotoClassic()
    elif userInput == "2":
        ClearSystem()
        main()
    elif userInput == "3":
        quit()
    else:
        ClearSystem()
        print("*****************\nChoix incorrect !\n*****************")
def LotoClassicLastResults():
    print("****************************\nDerniers resultats du Loto :\n****************************\n\nClassiques : 04 21 27 30 41\nChance : 06")
    userInput = input("\nMenu :\n1- Revenir au menu loto classique\n2- Revenir au menu principal\n3- Quitter l'application\n> ")
    if userInput == "1":
        ClearSystem()
        MenuLotoClassic()
    elif userInput == "2":
        ClearSystem()
        main()
    elif userInput == "3":
        quit()
    else:
        ClearSystem()
        print("*****************\nChoix incorrect !\n*****************")
def main():
    print("""****************************************************\n
 ██▓     ▒█████  ▄▄▄█████▓ ▒█████    ▄████  ▒█████  
▓██▒    ▒██▒  ██▒▓  ██▒ ▓▒▒██▒  ██▒ ██▒ ▀█▒▒██▒  ██▒
▒██░    ▒██░  ██▒▒ ▓██░ ▒░▒██░  ██▒▒██░▄▄▄░▒██░  ██▒
▒██░    ▒██   ██░░ ▓██▓ ░ ▒██   ██░░▓█  ██▓▒██   ██░
░██████▒░ ████▓▒░  ▒██▒ ░ ░ ████▓▒░░▒▓███▀▒░ ████▓▒░
░ ▒░▓  ░░ ▒░▒░▒░   ▒ ░░   ░ ▒░▒░▒░  ░▒   ▒ ░ ▒░▒░▒░ 
░ ░ ▒  ░  ░ ▒ ▒░     ░      ░ ▒ ▒░   ░   ░   ░ ▒ ▒░ 
  ░ ░   ░ ░ ░ ▒    ░      ░ ░ ░ ▒  ░ ░   ░ ░ ░ ░ ▒  
    ░  ░    ░ ░               ░ ░        ░     ░ ░  
                                                    
\n****************************************************""")
    choice = True
    while choice:
        userInput = input("\nMenu :\n1- Menu Loto classique\n2- Menu Grand Loto (en travaux)\n3- Menu Euro Million (en travaux)\n4- Quitter l'application\n> ")
        if userInput == "1":
            ClearSystem()
            MenuLotoClassic()
        elif userInput == "4":
            quit()
        else:
            ClearSystem()
            print("*****************\nChoix incorrect !\n*****************")
main()