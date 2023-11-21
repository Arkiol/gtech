import random

def initialisation(min=1, max=100):
    return random.randint(min, max)

def get_input(prompt: str):
    while True:
        try:
            value: int = int(input(prompt))
            return value
        except ValueError:
            print("Veuillez entrer un nombre")

def check_range(min_val, max_val):
    while True:
        if min_val < max_val:
            break
        else:
            print("Le nombre min doit être inférieur au nombre max")
            min_val: int = get_input("Veuillez entrer le nombre min: ")
            max_val: int = get_input("Veuillez entrer le nombre max: ")

    return min_val, max_val

def calculate_attempts(ecart):
    base_attempts: int = 2  
    max_attempts: int = 10  

    return min(base_attempts + (ecart // 10), max_attempts)


def play_round(min_val, max_val, max_attempts):
    guess_number: int = initialisation(min_val, max_val)
    attempts: int = 1

    print(f"Devinez le nombre entre {min_val} et {max_val}")
    while attempts <= max_attempts:
        answer = get_input("Votre réponse: ")
        if answer == guess_number:
            print("Félicitations")
            return True
        elif answer < guess_number:
            print("plus")
        else:
            print("moins")
        attempts += 1
    else:
        print("Défaite")
        return False

def play_game():
    min_val: int = get_input("Veuillez entrer le nombre min: ")
    max_val: int = get_input("Veuillez entrer le nombre max: ")
    min_val, max_val = check_range(min_val, max_val)
    rounds: int = get_input("Combien de manches voulez-vous jouer? ")
    ecart: int = max_val - min_val
    max_attempts: int = calculate_attempts(ecart)
    print(f"Vous avez {max_attempts} essais ")

    score: int = 0
    for _ in range(rounds):
        if play_round(min_val, max_val, max_attempts):
            score += 1
        print(f"Score actuel: {score}")

    print(f"Score final: {score}")

if __name__ == "__main__":
    while True:
        play_game()
        play_again: str = input("Voulez-vous jouer à nouveau? (Oui/Non): ")
        if play_again.upper() != "OUI":
            break