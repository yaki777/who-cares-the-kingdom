default world = World()
default battle_action_controller = BattleActionController()
default battle_controller = BattleController()
default npc_controller = NPCController()
default world_controller = WorldController()
default dungeon_controller = DungeonController()
label start:
    # 显示战斗
#     $ battle_controller.start()
#     call screen battle_screen
    $ npc_controller.gen_world_npc()
    $ npc_controller.update_npc_location()
    $ world_controller.step()
    call screen world_walk
#     $ dungeon_controller.step()
#     call screen dungeon_walk
#     call screen player_deck
#     call merchant_start
    jump next_scene

label next_scene:
    pass