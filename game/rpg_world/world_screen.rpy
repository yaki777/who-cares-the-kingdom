default npc_card_description = ""
default hovered_card = -1
default chosen_npc = None

screen world_walk:
    use card_table(world_controller.current_area.background,dungeon_controller.placed_card,dungeon_controller.player_hands,dungeon_controller.player_place_card)
