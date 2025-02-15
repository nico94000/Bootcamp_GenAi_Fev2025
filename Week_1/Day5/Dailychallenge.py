import random

class Game:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
    
    def get_user_item(self):
        while True:
            user_choice = input("Select (r)ock, (p)aper, or (s)cissors: ").lower()
            if user_choice in ['r', 'p', 's']:
                return {'r': 'rock', 'p': 'paper', 's': 'scissors'}[user_choice]
            print("Invalid choice. Please select 'r', 'p', or 's'.")
    
    def get_computer_item(self):
        return random.choice(self.choices)
    
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        if (user_item == "rock" and computer_item == "scissors") or \
           (user_item == "paper" and computer_item == "rock") or \
           (user_item == "scissors" and computer_item == "paper"):
            return "win"
        return "loss"
    
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        
        print(f"You selected {user_item}. The computer selected {computer_item}. You {result}!")
        return result
