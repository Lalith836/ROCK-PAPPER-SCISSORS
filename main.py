import random

def get_choices():
    options = ["rock","paper","scissors"]
    player_choice = input ("enter choice (rock,paper,scissors):").lower().strip()
    computer_choice = random.choice(options)
    choices = {
        "player" : player_choice ,
        "computer" : computer_choice
    }
    return choices 


def check_win(player , computer) :
    print (f"you chose {player} , computer chose {computer} ")
    if player == computer :
        return "tie"
    elif player == "rock": 
        if computer == "paper":
            return "computer win"
        else:
            return "player win"
    elif player == "paper":
        if  computer == "rock":
            return "player win"
        else:
            return "computer win"
    elif player == "scissors":
        if computer == "paper":
            return "player win"
        else:
             return "computer win"
    
choices = get_choices()
result = check_win(choices["player"] , choices["computer"])
print (result)
