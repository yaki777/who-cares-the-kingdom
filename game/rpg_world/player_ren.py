from rpg_role.roles_ren import ROLE_QUEEN

"""renpy
init 0 python:
"""


class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role


player = Player('Evelin', ROLE_QUEEN)
