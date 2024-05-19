from rpg_role.roles_ren import ROLE_QUEEN
from rpg_system.renpy_constant import Character

"""renpy
init 0 python:
"""


class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.c = Character(self.name)


player = Player('Evelin', ROLE_QUEEN)
