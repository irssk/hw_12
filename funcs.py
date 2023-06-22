from app import films
from app import main

def menu(films):
    choice = input("Please type 1 to get access to all films or 2 to return to the previous menu: ")
    if choice == "1":
        n = 0
        while n < len(films):
            print(n + 1)
            print('-'*34)
            print("Author: ", films[n]["author"])
            print("Rating: ", films[n]["rating"])
            print("Title: ", films[n]["title"])
            print("Id: ", films[n]["id"])
            print('-'*34)
            n = n + 1
    elif choice == "2":
        main()
    else:
        print("Wrong choice, buddy. You will have to start it all over again")
        menu(films)


def film_by_name(films):
    film = input("Please type the name of the film: ")
    n = 0
    flag = 0
    while n < len(films):
        if films[n]["title"] == film:
            print("Author: ", films[n]["author"])
            print("Rating: ", films[n]["rating"])
            print("Title: ", films[n]["title"])
            print("Id: ", films[n]["id"])
            flag = 1
            break
        n = n + 1
    if flag == 0:
        print("Sorry, we don't have this film")


def sorted_list(films):
    choice = input("Do you want to sort the films by rating from lower to higher(2) or from higher to lower(1)? ")
    if choice == "1":
        my_list = sorted(films, key=lambda k: k["rating"])
        n = 0
        while n < len(my_list):
            print('-'*34)
            print("Author: ", films[n]["author"])
            print("Rating: ", films[n]["rating"])
            print("Title: ", films[n]["title"])
            print("Id: ", films[n]["id"])
            print('-'*34)
            n = n + 1
    if choice == "2":
        my_list = sorted(films, key=lambda k: k["rating"])
        n = -1
        while abs(n) <= len(my_list):
            print('-'*34)
            print("Author: ", films[n]["author"])
            print("Rating: ", films[n]["rating"])
            print("Title: ", films[n]["title"])
            print("Id: ", films[n]["id"])
            print('-'*34)
            n = n - 1