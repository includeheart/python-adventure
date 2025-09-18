import random

def combat(inventory):
    print("You have entered the room with a monster! It's drooling with hunger, and notices your clunky movements.")
    while True:
        action = input("Do you want to (f)ight or (r)un away? ")
        if action == "f":
            # Pick a weapon from inventory
            weapon = "sword" if "sword" in inventory else ("dagger" if "dagger" in inventory else None)
            if not weapon:
                print("You have no suitable weapon!")
                continue

            roll = random.randint(1, 20)
            print(f'You roll a d20...Result: {roll}')

            if weapon == "sword":
                if roll >= 10:
                    print('You swing your sword and hit the monster!')
                else:
                    print('A swing and a miss!')
            elif weapon == "dagger":
                if roll >= 12:
                    print('You stab the monster with your dagger!')
                else:
                    print('You clumsily miss the monster!')
        else:  # action == "r"
            print('You run away from the monster!')
            break