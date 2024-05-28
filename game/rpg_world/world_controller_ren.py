import random

from rpg_battle.battle_action_library_ren import THEME_LOVE_LIBRARY, THEME_SELF_LIBRARY
from rpg_battle.battle_actions_ren import BattleAction
from rpg_cards.cards_ren import CARD_SUITS
from rpg_npc.npc_ren import NPC
from rpg_system.renpy_constant import npc_controller, story_controller, battle_action_controller
from rpg_world.area_ren import AREA_MAP, Area
from rpg_world.player_ren import player

"""renpy
init -100 python:
"""
from datetime import datetime, timedelta


class WorldController:
    def __init__(self):
        self.game_mode = 'v'
        self.allowed_organs = []
        self.allowed_toys = []
        self.current_area = AREA_MAP['cs1']
        self.player_hands = []
        self.placed_card = None
        self.date = datetime.strptime("1300-01-01 08:00:00", "%Y-%m-%d %H:%M:%S")

    def start_game(self):
        battle_action_controller.apply_filters(self.allowed_toys, self.allowed_organs)
        actions = []
        for perk in player.init_perks:
            actions += perk.init_actions()
        for action in actions:
            battle_action_controller.player_get_action(BattleAction(*action, level=random.randint(2, 11),
                                                                    suit=random.choice(CARD_SUITS)))
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
                npc_controller.talk_to_npc(card.addition)
                return
            if isinstance(self.placed_card.addition, Area):
                self.current_area = self.placed_card.addition
                self.date += timedelta(hours=1)
        story_controller.do_schedule()
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

    def get_hour(self):
        return self.date.hour

    def time_display(self):
        return (self.date.strftime('%mMonth%dDay %p %IHour')
                .replace('Month', '月')
                .replace('Day', '日')
                .replace('Hour', '点')
                .replace('PM', '下午')
                .replace('AM', '上午'))

    def place_player(self, area_code):
        self.current_area = AREA_MAP[area_code]
        self.step()

    def skip_date(self, days):
        self.date += timedelta(days=days)
        self.step()
