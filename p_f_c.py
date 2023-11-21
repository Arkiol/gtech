import random

def play_game():
    choices: int = {1: "pierre", 2: "feuille", 3: "ciseaux"}
    user_score: int = 0
    computer_score: int = 0

    while user_score < 3 and computer_score < 3:
        computer_choice: int = random.choice(list(choices.values()))
        user_choices = int(input("taper 1 pour pierre , 2 pour feuille , 3 pour ciseaux"))
        user_typing: str = choices[user_choices]

        print("votre choix est", user_typing)
        print("le choix de l'ordinateur est", computer_choice)

        if user_typing == computer_choice:
            print("Egalité")
        elif (user_typing == "pierre" and computer_choice == "ciseaux") or \
            (user_typing == "feuille" and computer_choice == "pierre") or \
            (user_typing == "ciseaux" and computer_choice == "feuille"):
            user_score += 1
            print("Victoire")
        else:
            computer_score += 1
            print("Défaite")

        print("Scores: Vous -", user_score, " Ordinateur -", computer_score)

    if user_score == 3:
        print("Vous avez gagné la partie!")
    else:
        print("L'ordinateur a gagné la partie!")

    play_again: str = input("rejouer ? (Oui/Non)")
    if play_again.upper() == "OUI":
        play_game()

play_game()
