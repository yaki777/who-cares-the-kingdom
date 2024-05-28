from rpg_role.roles_ren import *
from rpg_system.renpy_constant import Character
from rpg_world.init_perks_ren import PerkMasturbationLover

"""renpy
init 0 python:
"""


class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.init_perks = [PerkMasturbationLover()]
        self.c = Character(self.name)
        self.force = 0
        self.is_femboy = True
        self.has_goblin_antidote = False
        self.princess_is_virgin = True
        self.princess_agree_marry = None


PLAYER_ROLE_LIBRARY = [
    ROLE_QUEEN, ROLE_PRINCESS, ROLE_KNIGHT, ROLE_ADVENTURER, ROLE_NUN, ROLE_PROSTITUTE
]

player = Player('Evelin', ROLE_QUEEN)
