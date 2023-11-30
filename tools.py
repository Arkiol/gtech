from colorama import Fore, Style

def ask_int(prompt) -> int:
    while True:
        try:
            value: int = int(input(prompt))
            return value
        except ValueError:
            print("Ce n'est pas un nombre valide. Essayez encore.")

def ask_int_in_range(prompt, min_value, max_value):
    while True:
        value: int = ask_int(prompt)
            
        if min_value <= value <= max_value:
            return value
            
        print(f"Entrez un nombre entre {min_value} et {max_value}.")


#TODO Generaliser la fonction

'''
def main 
'''

def play_again() -> bool:
    play_again = ask_choice(f"Rejouer ? ({Fore.GREEN}Oui{Style.RESET_ALL}/{Fore.RED}Non{Style.RESET_ALL}): ", ["Oui", "Non", "OUI", "NON", "oui", "non"])
    return play_again.upper() == "OUI"



def ask_choice(prompt, valid_choices):
    while True:
        choice = input(prompt)
        if choice in valid_choices:
            return choice
        else:
            print("Ce n'est pas une option valide. Essayez encore.")
