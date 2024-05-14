from rpg_system.renpy_constant import world, npc_controller
from rpg_world.area_ren import AREA_MAP, Area

"""renpy
init -100 python:
"""


class WorldController:
    def __init__(self):
        self.world = world
        self.current_area = AREA_MAP['cs1']
        self.player_hands = []
        self.placed_card = None

    def player_place_card(self, card):
        self.placed_card = card
        self.player_hands.remove(card)

    def step(self, card):
        if card is not None:
            # if isinstance(card.addition,NPC):

            if isinstance(card.addition, Area):
                self.current_area = card.addition
        self.placed_card = None
        self.player_hands.clear()
        for area_code in self.current_area.links:
            area = AREA_MAP[area_code]
            self.player_hands.append(area.card)
        npc_list = npc_controller.get_area_npc_list(self.world.player_location)
        for npc in npc_list:
            self.player_hands.append(npc.card())

    def get_time(self):
        return self.world.current_hour
