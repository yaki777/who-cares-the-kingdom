default npc_card_description = ""
default hovered_card = -1
default chosen_npc = None
default world_reward_cards = None
label start_world(battle_result=None):
    python:
        world_reward_cards = None
        if battle_result is not None:
            world_reward_cards = world_controller.settle_battle_result(battle_result)
    call screen world_walk
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
    if world_controller.placed_card is not None and isinstance(world_controller.placed_card.addition,Area):
        use dm_say(f"你走向了{world_controller.placed_card.addition.name}",world_controller.step)
    if world_controller.placed_card is not None and isinstance(world_controller.placed_card.addition,NPC):
        use dm_say(f"你遇到了{world_controller.placed_card.addition.name}",world_controller.step)
    if world_reward_cards is not None:
        frame:
            style_prefix "say"
            xfill True
            yfill True
            background Solid("#000c",xfill=True,yfill=True)
            window:
                id "window"
                vbox:
                    text "DM" id "who"
                    text "选择一个奖励！" id "what"
        frame:
            background None
            xfill True
            yalign 0.4
            hbox:
                spacing 40
                xalign 0.5
                for card in world_reward_cards:
                    textbutton card.title:
                        style style.common_card
                        text_size 24
                        xsize 200
                        ysize 284
                        background Composite((200,284),
                            (0,0),Frame(card.background,
                                            yminimum=57, xminimum=57, yfill=True),
                            (0,0),Frame(card.inner,
                                            yminimum=57, xminimum=57, yfill=True))
                        action [Function(world_controller.player_choose_reward,card),SetVariable("world_reward_cards",None)]