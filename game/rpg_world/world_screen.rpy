default npc_card_description = ""
default hovered_card = -1
default chosen_npc = None
label start_world():
    call screen world_walk
    jump start_world
    return
screen world_walk:
    use card_table(world_controller.current_area.background,world_controller.placed_card,world_controller.player_hands,world_controller.player_place_card)

    frame:
        background None
        yalign 0.05
        xalign 0.5
        vbox:
            xalign 0.5
            text f"{world_controller.time_display()}":
                xalign 0.5
                text_align 0.5
                color "#FFF"
                outlines [ (0.5, "#333", 0, 0) ]
            text f"{world_controller.current_area.name}":
                xalign 0.5
                text_align 0.5
                color "#FFF"
                outlines [ (0.5, "#333", 0, 0) ]
            textbutton "等待一天":
                xalign 0.5
                action [Function(world_controller.skip_date,1)]
    if world_controller.placed_card is not None and isinstance(world_controller.placed_card.addition,Area):
        use dm_say(f"你走向了{world_controller.placed_card.addition.name}",world_controller.step)
    if world_controller.placed_card is not None and isinstance(world_controller.placed_card.addition,NPC):
        use dm_say(f"你遇到了{world_controller.placed_card.addition.name}",world_controller.step)