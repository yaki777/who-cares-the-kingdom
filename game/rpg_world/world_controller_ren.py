from rpg_system.renpy_constant import world, area_controller, renpy, npc_controller

"""renpy
init -100 python:
"""


class WorldController:
    def __init__(self):
        self.world = world

    def get_player_area_npc_list(self):
        return npc_controller.get_area_npc_list(self.world.player_location)

    def player_walk_menu(self):
        return area_controller.get_links(self.world.player_location)

    def player_walk_to(self, dest):
        self.world.player_location = dest.code
        npc_controller.update_npc_location()
        renpy.call("world_step")

    def get_time(self):
        return self.world.current_hour
