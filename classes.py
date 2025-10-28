"""This module defines the character classes available in the game, along with their attributes such as hit points (hp), starting inventory, and descriptions."""

classes = {
    'fighter': { 'hp': 8, 'inventory': ['metal armor', 'sword'], 'description' : 'You are strong and hardy, and excel in direct combat.' },
    'thief' : { 'hp' : 6, 'inventory' : ['leather armor', 'dagger'], 'description' : 'You are stealthy and agile, and excel at sneaking and stealing.' },
    'wizard' : { 'hp' : 4, 'inventory' : ['robes', 'spellbook'], 'description' : 'You are wise and powerful, and excel at casting spells.' }
}