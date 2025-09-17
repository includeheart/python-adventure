def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
You are an intrepid adventurer, on a quest to find a rare potion for a very important client.
Collect the potion, then make your way to the garden to escape.
But beware, a monster lurks, hungry for flesh.
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
  print("---------------------------")

inventory = []

## A dictionary linking a room to other rooms
rooms = {

  'Foyer' : {
    'north' : 'Hall',
    'description' : 'You are in the foyer of a mysterious home. The air is thick with dust and the scent of old wood. There is a door to the north.',
  },

  'Hall' : {
    'east'  : 'Dining Room',
    'north' : 'Bedroom',
    'west'  : 'Bathroom',
    'description' : 'You stand in the main hall of the mysterious home. The distinct scent of spent mana lingers in the air. There is a door to the south, east, north and west.',
  },
  'Kitchen' : {
    'north' : 'Dining Room',
    'south' : 'Garden',
    'down'  : 'Basement',
    'item'  : 'monster',
    'description' : 'You have entered the kitchen. The room is dimly lit by a flickering overhead light. There is a door to the north and a staircase leading down.',
  },
  'Dining Room' : {
    'west' : 'Hall',
    'south': 'Kitchen',
    'north' : 'Pantry',
    'description' : 'You are in the dining room. Dusty furniture and cobwebs fill the space. There is a door to the west, north and south.',
  },
  'Garden' : {
    'north' : 'Kitchen',
    'description' : 'You are in a lush garden, overgrown with weeds. The scent of flowers fills the air, but there is an eerie silence all around.'
  },
  'Pantry' : {
    'south' : 'Dining Room',
    'item' : 'dagger',
    'description2' : 'You are in the pantry. Shelves are lined with dusty jars and old food. There is a door to the south. There is a glint of metal on one of the shelves.',
    'description' : 'You are in the pantry. Shelves are lined with dusty jars and old food. There is a door to the south.'
  },
  'Bedroom' : {
    'south' : 'Hall',
    'item' : 'key',
    'description2' : 'You are in the bedroom. The bed is unmade and the curtains are drawn. There is a door to the south. You spot a key on the bedside table.',
    'description' : 'You are in the bedroom. The bed is unmade and the curtains are drawn. There is a door to the south.'
  },
  'Bathroom' : {
    'east' : 'Hall',
    'description' : 'You are in the bathroom. The air is humid and the sound of dripping water echoes around you. There is a door to the east.'
  },
  'Basement' : {
    'up' : 'Kitchen',
    'description2' : 'You are in the basement. The air is musty and the only light comes from a small window near the ceiling. There is a staircase leading up. Tucked in the corner is a small chest with a lock.',
    'description' : 'You are in the basement. The air is musty and the only light comes from a small window near the ceiling. There is a staircase leading up.'
  }
}

items = {
  'key' : 'A small, rusty key. It may unlock something important.',
  'dagger' : 'A sharp, silver dagger. It gleams in the dim light. Better safe than sorry!',
  'potion' : 'A vial of glowing green liquid. It looks very valuable. This must be the rare potion you were hired to find.',
  'dead monster' : 'The slain monster lies motionless on the ground, its menacing presence finally subdued.'
}

#start the player in the Foyer
currentRoom = 'Foyer'

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
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'dagger' not in inventory:
    print('You have entered the room with a monster! It\'s drooling with hunger, and notices your clunky movements.')
    print('A monster has eaten you... GAME OVER!')
    break
  
  ## If a player has the dagger and encounters a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'dagger' in inventory:
    del rooms[currentRoom]['item']
    rooms[currentRoom]['item'] = 'dead monster'
    print('You have entered the room with a monster! It\'s drooling with hunger, and notices your clunky movements.')
    print('You have slain the monster with your dagger!')

  if currentRoom == 'Basement' and 'key' in inventory and 'potion' not in inventory:
    print('You use the key to unlock the chest, revealing the rare potion inside.')
    inventory.append('potion')
  elif currentRoom == 'Basement' and 'key' not in inventory and 'potion' not in inventory:
    print('You see a locked chest here. You need a key to open it.')
  elif currentRoom == 'Basement' and 'potion' in inventory:
    print('The chest is open and empty now. You have already taken the potion.')