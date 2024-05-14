from rpg_world.area_ren import AREA_MAP

"""renpy
init -100 python:
"""


class AreaController:
    def __init__(self):
        self.area_map = AREA_MAP

    def get_links(self, code):
        links = []
        for link in self.area_map[code].links:
            links.append(self.area_map[link])
        return links
