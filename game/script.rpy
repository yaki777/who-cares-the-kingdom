default card_library = []
default world = World()
default cards_controller = CardsController()
default battle_controller = BattleController()
default area_controller = AreaController()
default npc_controller = NPCController()
default world_controller = WorldController()
default dungeon_controller = DungeonController()
label start:
    # 显示战斗
#     $ battle_controller.start()
#     call screen battle_screen
#     $ npc_controller.gen_world_npc()
    $ npc_controller.update_npc_location()
    call screen world_step
#     $ dungeon_controller.step()
#     call screen dungeon_walk
    call screen player_deck
    jump next_scene

label next_scene:
    # 下一个场景的逻辑
    pass