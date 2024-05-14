from rpg_system.base_ren import SexualColor

"""renpy
init -100 python:
"""
from enum import Enum

world_mode = {
    "v": ("这是一个虚拟的游戏，你不需要在现实世界做出行动", SexualColor.LV2),
    "r": ("这是一个现实的游戏，当你的角色在游戏中行动时，你也要在现实中进行与之匹配的行动", SexualColor.LV3)
}


class Faction(Enum):
    Zephyria = ("泽菲利亚", "Zephyria")
    Ferrox = ("费罗克斯", "Ferrox")
    Seraphine = ("瑟拉芬", "Seraphine")


class World(object):
    def __init__(self, mode="v"):
        self.mode = mode
        self.current_hour = 7
        self.current_day = 1
        self.player_location = 'uk'

    def get_time(self):
        return f"第{self.current_day}天 {self.current_hour}时"
