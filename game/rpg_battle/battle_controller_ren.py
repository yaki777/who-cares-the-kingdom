from rpg_battle.battle_action_controller_ren import BattleActionController
from rpg_battle.battle_actions_ren import THEME_LOVE, THEME_MACHINE
from rpg_battle.battle_calculator_ren import BattleCalculator
from rpg_cards.cards_ren import CARD_SLOT
from rpg_system.renpy_constant import battle_action_controller, renpy, world_controller

"""renpy
init -80 python:
"""
import random


class BattleController:

    def __init__(self):
        self.player_hand = []
        self.enemy = None
        self.player_table = [CARD_SLOT, CARD_SLOT, CARD_SLOT, CARD_SLOT, CARD_SLOT]
        self.enemy_table = [CARD_SLOT, CARD_SLOT, CARD_SLOT, CARD_SLOT, CARD_SLOT]
        self.player_rank = 0
        self.player_chips = 3
        self.round = 1
        self.player_table_desc = ''
        self.enemy_table_desc = ''
        self.battle_info = ''
        self.halftime = None
        self.theme = THEME_LOVE
        self.battle_calculator = BattleCalculator()

    def clear_battle(self):
        self.player_hand = []
        self.enemy = None
        self.player_table = [CARD_SLOT, CARD_SLOT, CARD_SLOT, CARD_SLOT, CARD_SLOT]
        self.enemy_table = [CARD_SLOT, CARD_SLOT, CARD_SLOT, CARD_SLOT, CARD_SLOT]
        self.player_rank = 0
        self.player_chips = 3
        self.round = 1
        self.player_table_desc = ''
        self.enemy_table_desc = ''
        self.battle_info = ''
        self.halftime = None
        self.theme = THEME_LOVE
        self.battle_calculator = BattleCalculator()

    def player_table_len(self):
        return len([card for card in self.player_table if card.addition is not None])

    def player_play_card(self, card):
        self.player_hand.remove(card)
        for i, slot in enumerate(self.player_table):
            if slot.addition is None:
                self.player_table[i] = card
                break
        player_table_rank, player_table_score = self.battle_calculator.get_max_table(self.player_table)
        self.player_table_desc = f'{player_table_rank[1]}: {player_table_score}'

    def player_return_card(self, card):
        if card.addition is None:
            return
        for i, slot in enumerate(self.player_table):
            if slot == card:
                self.player_table[i] = CARD_SLOT
                break
        self.player_hand.append(card)
        if len(self.player_hand) < 5:
            player_table_rank, player_table_score = self.battle_calculator.get_max_table(self.player_table)
            self.player_table_desc = f'{player_table_rank[1]}: {player_table_score}'

    def enemy_play_card(self):
        numbers = [1, 2, 3, 4, 5]
        weights = [5, 4, 3, 2, 1]
        card_number = random.choices(numbers, weights, k=1)[0]
        cards = battle_action_controller.enemy_draw_cards(self.enemy.id, card_number, self.theme)
        for card in cards:
            for i, slot in enumerate(self.enemy_table):
                if slot.addition is None:
                    self.enemy_table[i] = card
                    break
        enemy_table_rank, enemy_table_score = self.battle_calculator.get_max_table(self.enemy_table)
        self.enemy_table_desc = f'{enemy_table_rank[1]}: {enemy_table_score}'

    def start(self, enemy):
        self.clear_battle()
        self.enemy = enemy
        if world_controller.current_area.code == 'al1':
            self.theme = THEME_MACHINE
        battle_action_controller.player_shuffle_deck()
        battle_action_controller.enemy_shuffle_deck(self.enemy.id)
        self.player_hand = battle_action_controller.player_draw_cards(5, self.theme)
        self.enemy_play_card()
        self.battle_info = f'回合 {self.round}'

        renpy.call("start_battle")

    def result_display(self):
        text = []
        if self.player_chips == 0:
            text.append("战斗结束，你的筹码用完了。")
        elif self.player_rank >= self.enemy.hp:
            text.append("战斗胜利！")
        return text

    def is_win(self):
        return self.enemy.hp <= self.player_rank

    def settle_battle_result(self):
        battle_result = ['win' if self.enemy.hp <= self.player_rank else "lose", self.enemy, self.player_rank]
        result = battle_result[0]
        enemy = battle_result[1]
        if result == 'win':
            return battle_action_controller.enemy_draw_cards(enemy.id, 3, self.theme)
        return None

    def is_end(self):
        return self.player_chips == 0 or self.player_rank >= self.enemy.hp

    def end_turn(self):
        player_table_rank, player_table_score = self.battle_calculator.get_max_table(self.player_table)
        enemy_table_rank, enemy_table_score = self.battle_calculator.get_max_table(self.enemy_table)
        player_win = True
        if player_table_rank[0] < enemy_table_rank[0]:
            player_win = False
        elif player_table_rank[0] == enemy_table_rank[0]:
            if player_table_score < enemy_table_score:
                player_win = False
        table = self.player_table
        if not player_win:
            table = self.enemy_table
            self.player_chips -= 1
        cards = [card for card in table if card.addition is not None]
        self.halftime = BattleHalftime(self, player_win, cards)
        self.round += 1
        self.battle_info = f'回合 {self.round}'
        self.player_table = [CARD_SLOT, CARD_SLOT, CARD_SLOT, CARD_SLOT, CARD_SLOT]
        self.enemy_table = [CARD_SLOT, CARD_SLOT, CARD_SLOT, CARD_SLOT, CARD_SLOT]
        self.enemy_play_card()
        for card in battle_action_controller.player_draw_cards(5 - len(self.player_hand), self.theme):
            self.player_hand.append(card)
        if self.player_chips == 0:
            self.battle_info = '战斗结束!'


class BattleHalftime:
    def __init__(self, battle_controller, player_win, cards):
        self.battle_controller = battle_controller
        self.player_win = player_win
        self.cards = cards
        self.current_card = None

    def step(self):
        self.current_card = self.cards.pop(0)
        rank = self.current_card.addition.exp
        is_weakness = any(i in self.battle_controller.enemy.weakness for i in self.current_card.addition.tags)
        if is_weakness:
            rank *= 2
        self.battle_controller.player_rank += rank
        if self.battle_controller.player_rank >= self.battle_controller.enemy.hp:
            self.battle_controller.battle_info = '战斗胜利!'

    def end(self):
        self.battle_controller.halftime = None
