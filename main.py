from rooms import rooms
from items import items
from classes import classes as character_classes

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
You are an intrepid adventurer, on a quest to find a rare potion for a very important client.
The potion is rumored to be in the posession of an old, retired alchemist who lives in a mysterious house.
Strange noises and lights sometimes emanate from the dusty windows, leaving the peasentry to whisper about dark magic and unspeakable rituals.
Casing the house, you know the alchemist has left his home for the day, leaving you a small window of opportunity to sneak in and find the potion.
Whether you had to swallow your fears of the unknown, or boldy ventured forth, you have easily picked the lock and stepped inside.
Explore with caution, the magically inclined are known to set deadly traps or keep dangerous familiars.
Commands:
  go [direction] (walk in the given direction)
  get [item] (pick up an item)
  examine [item] (inspect an item)
  drop [item] (drop an item)
  look (look around the room)
  quit (exit the game)
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print('---------------------------')

# --- Character Creation ---
def create_character():
  print('''
Character Creation
------------------
Enter your name, then choose a class. Your starting inventory and HP will be set based on your choice.
''')
  # Get a non-empty name
  name = ''
  while not name.strip():
    name = input('Enter your name: ').strip()

  # Show available classes
  print('\nAvailable classes:')
  for cname, cinfo in character_classes.items():
    print(f"  - {cname.title()}: {cinfo['description']} (HP: {cinfo['hp']}, Items: {', '.join(cinfo['inventory'])})")

  # Choose class
  chosen = ''
  valid_names = {k.lower(): k for k in character_classes.keys()}
  while True:
    chosen = input("Choose your class (fighter/thief/wizard): ").strip().lower()
    if chosen in valid_names:
      chosen = valid_names[chosen]
      break
    print('Invalid class. Please type fighter, thief, or wizard.')

  details = character_classes[chosen]
  # Copy inventory list to avoid mutating source
  start_inventory = list(details['inventory'])
  hp = details['hp']

  print(f"\nWelcome, {name} the {chosen.title()}!")
  print(details['description'])
  print(f"Starting HP: {hp}")
  print(f"Starting Items: {', '.join(start_inventory)}\n")

  return name, chosen, hp, start_inventory

#start the player in the Foyer
currentRoom = 'Foyer'

# Create the character before starting the game
player_name, player_class, hp, inventory = create_character()

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory.append(move[1])
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  if move[0] == 'look':
    if 'item' in rooms[currentRoom]:
      print(rooms[currentRoom]['description2'])
    else:
      print(rooms[currentRoom]['description'])
  
  if move[0] == 'examine':
    if move[1] in inventory:
      print(items[move[1]])
    else:
      print('You don\'t have a ' + move[1] + ' to examine.')
  
  if move[0] == 'drop':
    if move[1] in inventory:
      inventory.remove(move[1])
      if 'item' in rooms[currentRoom]:
        print('You can\'t drop ' + move[1] + ' here, there is already a ' + rooms[currentRoom]['item'] + ' present.')
        inventory.append(move[1])
      else:
        rooms[currentRoom]['item'] = move[1]
        print('You have dropped the ' + move[1] + '.')
    else:
      print('You don\'t have a ' + move[1] + ' to drop.')
    
  if move[0] == 'quit':
    print('Thanks for playing!')
    break

  ## Define how a player can win
  if currentRoom == 'Garden' and 'potion' in inventory:
    print('You\'ve escaped the house with the magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  if 'monsters' in rooms[currentRoom] and 'dagger' not in inventory:
    print('You have entered the room with a monster! It\'s drooling with hunger, and notices your clunky movements.')
    print('A monster has eaten you... GAME OVER!')
    break
  
  ## If a player has the dagger and encounters a monster
  elif 'monsters' in rooms[currentRoom] and'dagger' in inventory:
    del rooms[currentRoom]['monsters']
    print('You have entered the room with a monster! It\'s drooling with hunger, and notices your clunky movements.')
    print('You have slain the monster with your dagger!')

  if currentRoom == 'Basement' and 'key' in inventory and 'potion' not in inventory:
    print('You use the key to unlock the chest, revealing the rare potion inside.')
    inventory.append('potion')
  elif currentRoom == 'Basement' and 'key' not in inventory and 'potion' not in inventory:
    print('You see a locked chest here. You need a key to open it.')
  elif currentRoom == 'Basement' and 'potion' in inventory:
    print('The chest is open and empty now. You have already taken the potion.')