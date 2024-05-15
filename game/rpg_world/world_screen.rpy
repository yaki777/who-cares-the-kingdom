default npc_card_description = ""
default hovered_card = -1
default chosen_npc = None

screen world_walk:
    use card_table(world_controller.current_area.background,world_controller.placed_card,world_controller.player_hands,world_controller.player_place_card)
    if world_controller.placed_card is not None and isinstance(world_controller.placed_card.addition,Area):
        use dm_say(f"你走向了{world_controller.placed_card.addition.name}",world_controller.step)