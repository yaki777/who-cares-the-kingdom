from rpg_battle.battle_action_controller_ren import BattleActionController
from rpg_battle.battle_controller_ren import BattleController
from rpg_dungeon.dungeon_controller_ren import DungeonController
from rpg_npc.npc_controller_ren import NPCController
from rpg_story.story_ren import StoryController
from rpg_world.world_controller_ren import WorldController


world_controller = WorldController()
npc_controller = NPCController()
battle_action_controller = BattleActionController()
battle_controller = BattleController()
story_controller = StoryController()
dungeon_controller = DungeonController()

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

    def return_statement(self, value=None):
        pass
    def loadable(self,filename, directory=None):
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
