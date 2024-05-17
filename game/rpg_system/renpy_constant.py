from rpg_battle.battle_action_controller_ren import BattleActionController
from rpg_battle.battle_controller_ren import BattleController
from rpg_npc.npc_controller_ren import NPCController
from rpg_world.world_controller_ren import WorldController
from rpg_world.world_ren import World

world = World()

world_controller = WorldController()
npc_controller = NPCController()
battle_action_controller = BattleActionController()
battle_controller = BattleController()


class Renpy:
    def say(self, who, what, *args, **kwargs):
        pass

    def call(self, label, *args, from_current=False, **kwargs):
        pass

    def scene(self, layer='master'):
        pass

    def show(name, at_list=[], layer=None, what=None, zorder=0, tag=None, behind=[], **kwargs):
        pass

    def call_screen(self, _screen_name, *args, _with_none=True, _mode='screen', **kwargs):
        pass

    def display_menu(self, items, *, interact=True, screen='choice', type='menu', _layer=None, **kwargs):
        pass

    def has_label(self, name):
        pass


renpy = Renpy()


def narrator(*args, **kwargs):
    pass


def say(*args, **kwargs):
    pass


def Character(*args, **kwargs):
    pass


def menu(*args, **kwargs):
    pass


npc_list = []
