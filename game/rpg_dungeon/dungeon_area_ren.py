"""renpy
init -45 python:
"""


class DungeonArea:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.background = f"images/dungeon/{name}.png"


DUNGEON_AREAS = [
    DungeonArea("dungeon_forest", "森林"),
    DungeonArea("dungeon_pool", "池塘"),
    DungeonArea("dungeon_castle", "城堡"),
    DungeonArea("dungeon_village", "村庄"),
]
