from utils import random_id
from funcs import *

films = [
    {"author": "TheBrianMaps",
     "rating": "1000",
     "title": "Last Button 2",
     "id": random_id.get_random_id()
    },
    {"author": "Young Sang Ho",
     "rating": "10",
     "title": "Train to Busan",
     "id": random_id.get_random_id()
    },
    {"author": "Justin Baldoni",
     "rating": "9",
     "title": "One meter apart",
     "id": random_id.get_random_id()
    },
    {"author": "Stephen King",
     "rating": "8",
     "title": "It",
     "id": random_id.get_random_id()
    },
    {"author": "James Cameron",
     "rating": "7",
     "title": "Titanic",
     "id": random_id.get_random_id()
     }
]

def main():
    choice = input("Hello, user! 1 for menu, 2 for film by name, 3 for sorted list: ")
    if choice == "1":
        menu(films)
    elif choice == "2":
        film_by_name(films)
    elif choice == "3":
        sorted_list(films)
    else:
        print("Wrong choice, buddy")
        main()


if __name__ == "__main__":
    main()