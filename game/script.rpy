default DM = Character("DM")
default battle_action_controller = BattleActionController()
default battle_controller = BattleController()
default npc_controller = NPCController()
default world_controller = WorldController()
default dungeon_controller = DungeonController()
default story_controller = StoryController()
label start:
#     call init_player
    # 显示战斗
    $ world_controller.allowed_toys = TOY_LIBRARY
    $ world_controller.allowed_organs = ORGAN_LIBRARY
    $ world_controller.start_game()
    $ story_controller.start()
#     $ story_controller.start_stage("S_GS_stage_1")
    call start_world
#     $ dungeon_controller.start(2)
#     call screen dungeon_walk

#     call screen player_deck

    jump next_scene

label next_scene:
    pass