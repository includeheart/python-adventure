"""This module defines the rooms in the adventure game, including their connections, descriptions, and any items or monsters present."""

from monsters import monsters

rooms = {

  'Foyer' : {
    'north' : 'Hall',
    'description' : 'You are in the foyer of a mysterious home. The air is thick with dust and the scent of old wood. There is a door to the north, and a staircase leading up into darkness.'
  },

  'Hall' : {
    'east'  : 'Dining Room',
    'north' : 'Bedroom',
    'west'  : 'Bathroom',
    'description' : 'You stand in the main hall of the mysterious home. The distinct scent of spent mana lingers in the air. There is a door to the south, east, north and west.'
  },
  'Kitchen' : {
    'north' : 'Dining Room',
    'south' : 'Garden',
    'down'  : 'Basement',
    'monsters' : monsters['displacer_beast'],
    'description' : 'You have entered the kitchen. The room is dimly lit by a flickering overhead light. There is a door to the north and a staircase leading down.'
  },
  'Dining Room' : {
    'west' : 'Hall',
    'south': 'Kitchen',
    'north' : 'Pantry',
    'description' : 'You are in the dining room. Dusty furniture and cobwebs fill the space. There is a door to the west, north and south.'
  },
  'Garden' : {
    'north' : 'Kitchen',
    'description' : 'You are in a lush garden, overgrown with weeds. The scent of flowers fills the air, but there is an eerie silence all around.'
  },
  'Pantry' : {
    'south' : 'Dining Room',
    'item' : 'health potion',
    'description2' : 'You are in the pantry. Shelves are lined with dusty jars and old food. There is a door to the south. There is a small bottle filled with a shimmering red liquid on one of the shelves.',
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