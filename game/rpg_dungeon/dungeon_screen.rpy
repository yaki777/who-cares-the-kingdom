label start_dungeon:
    python:
        card_table_hovered_card = None
        card_table_chosen_card = None
        dungeon_controller.placed_card = None
    call screen dungeon_walk
    call start_dungeon
screen dungeon_walk:
    use card_table(dungeon_controller.current_area.background,dungeon_controller.placed_card,dungeon_controller.player_hands,dungeon_controller.player_place_card)
    # 选择敌人
    if dungeon_controller.placed_card is not None and isinstance(dungeon_controller.placed_card.addition,NPC):
        use dm_say(f"{dungeon_controller.placed_card.addition.name}发现你了！",dungeon_controller.step)
    # 选择路线
    if dungeon_controller.placed_card is not None and isinstance(dungeon_controller.placed_card.addition,DungeonArea):
        use dm_say(f"你继续深入，走到了一片{dungeon_controller.placed_card.addition.title}",dungeon_controller.step)
    # 离开副本
    if dungeon_controller.placed_card is not None and dungeon_controller.placed_card.addition is None:
        use dm_say("是时候回家了","Return()")