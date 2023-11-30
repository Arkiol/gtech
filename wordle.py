import random
import re
from tools import *

# Données
data = ["pomme", "peche", "olive", "malte", "plage", "cedre", "baies", "melon", "hetre", "marre"]

def get_word(data):
    word_to_guess = random.choice(data)
    return word_to_guess

def grid_init():
    grid = []
    for row in range(6):
        grid.append(['_'] * 5)
    return grid

def grid_display(grid):
    for row in grid:
        print('  '.join(row))

def ask_input():
    while True:
        user_input = input("Entrez un mot : ")
        
        if user_input not in data:
            print("Ce mot n'est pas dans la liste.")
            continue

        if not re.match("^[a-zA-Z]*$", user_input):
            print("Ce n'est pas un mot")
            continue 

        if len(user_input) != 5:
            print("Le mot doit contenir exactement 5 lettres")
            continue

        return user_input

def get_letter(user_input, word_to_guess, grid, attempt):
    for i in range(5):
        if user_input[i] == word_to_guess[i]:
            grid[attempt][i] = "\033[92m" + user_input[i].upper() + "\033[0m"
        elif user_input[i] in word_to_guess:
            grid[attempt][i] = "\033[93m" + user_input[i].upper() + "\033[0m"
    return grid

def play():
    print(f"Voici la liste de mots : {data}")
    print("Dans cette liste, trouvez le mot exact")

    word_to_guess = get_word(data)
    grid = grid_init()

    for attempt in range(6):
        grid_display(grid)
        
        user_input = ask_input()
        
        if user_input.lower() == word_to_guess:
            print(f"Bravo ! Vous avez trouvé le mot : {word_to_guess}")
            break
        else:
            print(f"Ce n'est pas le bon mot. Il vous reste {5 - attempt} tentatives.")
            
            attempt -= 1 if user_input in data else 0

        grid[attempt] = list(user_input.upper()) 
        grid = get_letter(user_input, word_to_guess, grid, attempt)

    else:
        print(f"Désolé, vous avez épuisé toutes vos tentatives. Le mot à trouver était : {word_to_guess}")
    
    while True:
        if  play_again():
            play()
        else : 
            break

play()
