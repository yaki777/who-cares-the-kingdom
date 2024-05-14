default dungeon_reward_cards = None
label start_dungeon(battle_result=None):
    python:
        dungeon_rewards = None
        if battle_result is not None:
            dungeon_reward_cards = dungeon_controller.settle_battle_result(battle_result)
        card_table_hovered_card = None
        card_table_chosen_card = None
        dungeon_controller.placed_card = None
    call screen dungeon_walk
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
    # 奖励
    if dungeon_reward_cards is not None:
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
                for card in dungeon_reward_cards:
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
                        action [Function(dungeon_controller.player_choose_reward,card),SetVariable("dungeon_reward_cards",None)]