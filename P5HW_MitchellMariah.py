#Mariah Mitchell
#12 May 2025
#P5HW
#program a adventure game using loops and functions
import random
import time



class Character:
    def __init__(self, name, role, skill,):
        self.name = name
        self.role = role
        self.skill = skill

    def show_summary(self):
        print("\n🧾 Character Summary:")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Skill: {self.skill}")
        print("\nYou're ready to start your boat adventure!")

def choose_option(prompt, options):
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("Choose an option (1/2/3): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")

def create_character():
    print("🚢 Welcome to the Adventure Boat Game")
    
    name = input("What is your character's name? ")

    role = choose_option("\nChoose your role:", [
        "Captain - Commands the crew and makes key decisions.",
        "Engineer - Repairs and maintains the ship.",
        "Navigator - Charts the safest and quickest course."
    ])

    skill = choose_option("\nChoose a special skill:", [
        "Leadership - Boosts team morale and cooperation.",
        "Mechanics - Can fix almost anything.",
        "Survival - Great instincts in dangerous situations."
    ])


    character = Character(name, role, skill,)
    character.show_summary()

if __name__ == "__main__":
    create_character()
    
#player choose which route to take
def get_player_choice():
    print("\nChoose your direction:")
    print("1. Left")
    print("2. Center")
    print("3. Right")
    choice = input("Enter 1, 2, or 3: ")
    #if choice is not 1, 2, or 3. Invalid choice
    while choice not in ["1", "2", "3"]:
        #Correction statement is implemented
        choice = input("Invalid input. Please enter 1, 2, or 3: ")
    return int(choice)

def check_path(player_choice, safe_path, has_jewels):
    if player_choice == safe_path:
        print("You safely pass through this part of the river.")
        if has_jewels:
            print("🎉 You found the lost jewels floating in the river!")
            return "win"
        return "continue"
    else:
        print("💥 Oh no! You hit an obstacle and your boat sank.")
        return "lose"
    intro()

    
#Create loop
def adventure_game():
    #Number of turns
    turns = 5
    #made a sequence from 1 to 5; runs once for each turn
    for turn in range(1, turns + 1):
        print(f"\n-- Turn {turn} --")
        safe_path = random.randint(1, 3)#Represents a possible river path
        has_jewels = (turn == random.randint(2, turns))  #Random jewels chance after turn 1
        player_choice = get_player_choice()
        result = check_path(player_choice, safe_path, has_jewels)
        if result == "win":
            print("🏆 Congratulations! You've completed the adventure and won the game!")
            break
        elif result == "lose":
            print("☠️ Game Over. Better luck next time!")
            break
        else:
            print("🚣‍♂️ You continue paddling down the river...")
            time.sleep(1)
    else:
        print("\n⛵ You reached the end of the river but didn’t find the treasure.")
        print("Thanks for playing!")

if __name__ == "__main__":
    adventure_game()
