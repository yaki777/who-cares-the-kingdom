"""renpy
init -45 python:
"""


class DungeonArea:
    def __init__(self, name, title, theme, is_theme_entry=False, is_theme_exit=False):
        self.name = name
        self.title = title
        self.background = f"images/dungeon/{name}.png"
        self.theme = theme
        self.is_theme_entry = is_theme_entry
        self.is_theme_exit = is_theme_exit


DUNGEON_AREAS = [
    DungeonArea("dungeon_road0", "小路", 'base'),
    DungeonArea("dungeon_road1", "小路", 'base'),
    DungeonArea("dungeon_road2", "小路", 'base'),
    DungeonArea("dungeon_road3", "小路", 'base'),
    DungeonArea("dungeon_road4", "小路", 'base'),
    DungeonArea("dungeon_road5", "小路", 'base'),
    DungeonArea("dungeon_castle0", "城堡入口", 'castle', is_theme_entry=True),
    DungeonArea("dungeon_castle1", "城堡某处", "castle"),
    DungeonArea("dungeon_castle2", "城堡某处", "castle"),
    DungeonArea("dungeon_castle3", "城堡某处", "castle"),
    DungeonArea("dungeon_castle4", "城堡某处", "castle"),
    DungeonArea("dungeon_castle5", "城堡出口", 'castle', is_theme_exit=True),
    DungeonArea("dungeon_cave0", "洞穴入口", 'cave', is_theme_entry=True),
    DungeonArea("dungeon_cave1", "洞穴某处", "cave"),
    DungeonArea("dungeon_cave2", "洞穴某处", "cave"),
    DungeonArea("dungeon_cave3", "洞穴某处", "cave"),
    DungeonArea("dungeon_cave4", "洞穴某处", "cave"),
    DungeonArea("dungeon_cave5", "洞穴出口", 'cave', is_theme_exit=True),
    DungeonArea("dungeon_forest0", "森林入口", 'forest', is_theme_entry=True),
    DungeonArea("dungeon_forest1", "森林某处", "forest"),
    DungeonArea("dungeon_forest2", "森林某处", "forest"),
    DungeonArea("dungeon_forest3", "森林某处", "forest"),
    DungeonArea("dungeon_forest4", "森林某处", "forest"),
    DungeonArea("dungeon_forest5", "森林出口", 'forest', is_theme_exit=True),

]
