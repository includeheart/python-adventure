"""This module defines the monsters that players may encounter in the game, along with their attributes such as hit points (hp), damage potential, and size."""

from random import randint

monsters = {
    'displacer_beast' : { 'name' : 'Displacer Beast', 'hp' : 12, 'damage' : randint(2, 8), 'size' : 'large'}
}