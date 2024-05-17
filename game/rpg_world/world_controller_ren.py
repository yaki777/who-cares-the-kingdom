from rpg_npc.npc_ren import NPC
from rpg_system.renpy_constant import world, npc_controller, renpy, battle_action_controller
from rpg_world.area_ren import AREA_MAP, Area

"""renpy
init -100 python:
"""
from datetime import datetime, timedelta


class WorldController:
    def __init__(self):
        self.world = world
        self.current_area = AREA_MAP['cs1']
        self.player_hands = []
        self.placed_card = None
        self.date = datetime.strptime("1300-01-01 08:00:00", "%Y-%m-%d %H:%M:%S")

    def start_game(self):
        npc_controller.gen_world_npc()
        npc_controller.update_npc_location()
        self.step()

    def player_place_card(self, card):
        self.placed_card = card
        self.player_hands.remove(card)

    def step(self):
        if self.placed_card is not None:
            if isinstance(self.placed_card.addition, NPC):
                card = self.placed_card
                self.player_hands.append(self.placed_card)
                self.placed_card = None
                # renpy.call("npc_talk", self.current_area.background,card.addition,card.addition.label)
                npc_controller.talk_to_npc(card.addition.id)
                return
            if isinstance(self.placed_card.addition, Area):
                self.current_area = self.placed_card.addition
                self.date += timedelta(hours=1)
        if self.date.hour in [3, 6, 9, 12, 15, 18, 21, 0]:
            npc_controller.update_npc_location()
        self.placed_card = None
        self.player_hands.clear()
        for area_code in self.current_area.links:
            area = AREA_MAP[area_code]
            self.player_hands.append(area.card())
        npc_list = npc_controller.get_area_npc_list(self.current_area.code)
        for npc in npc_list:
            self.player_hands.append(npc.card())

    def settle_battle_result(self, battle_result):
        result = battle_result[0]
        enemy = battle_result[1]
        player_rank = battle_result[2]
        if result == 'win':
            return battle_action_controller.enemy_draw_cards(enemy.id, 3)

    def player_choose_reward(self, card):
        battle_action_controller.player_get_action(card.addition)

    def get_time(self):
        return self.world.current_hour
