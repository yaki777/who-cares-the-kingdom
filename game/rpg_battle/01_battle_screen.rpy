default card_description = ""
default battle_hovered_card = None
default battle_reward_cards = None
label start_battle():
    DM "战斗开始！"
    python:
        card_description = ""
        battle_hovered_card = None
    call start_battle_screen
    call after_battle_screen
    return
label start_battle_screen:
    call screen battle_screen
    return

label after_battle_screen:
    $ battle_reward_cards = battle_controller.settle_battle_result()
    if battle_reward_cards is not None:
        call screen battle_reward
    return
screen battle_screen:
    add "images/table_bg.png"

    frame:
        background None
        xfill True
        vbox:
            xalign 0.5
            spacing 20
            label "得分:"
            hbox:
                bar value battle_controller.player_rank range battle_controller.enemy.hp xysize (1000,20)
    frame:
        background None
        ysize 500
        xfill True
        yalign 0.2
        vbox:
            xalign 0.5
            spacing 20
            label f"敌人的行动({battle_controller.enemy_table_desc}):" xalign 0.5
            hbox:
                xalign 0.5
                spacing 10
                box_wrap True
                xmaximum 1080
                for card in battle_controller.enemy_table:
                    if isinstance(card, CardSlot):
                        textbutton "":
                            text_size 24
                            xsize 200
                            ysize 284
                            background Frame(card.background,yminimum=57, xminimum=57, yfill=True)
                            action [NullAction()]
                    else:
                        textbutton card.title:
                            style style.common_card
                            text_size 24
                            xsize 200
                            ysize 284
                            background Composite((200,284),
                                            (0,0),Frame(card.background,
                                                            yminimum=57, xminimum=57, yfill=True),
                                            (0,0),Frame(card.inner,
                                                            yminimum=57, xminimum=57))
                            action [NullAction()]
    frame:
        background None
        yalign 0.45
        xfill True
        label battle_controller.battle_info xalign 0.5

    frame:
        background None
        xfill True
        ysize 500
        yalign 0.72
        vbox:
            hbox:
                xalign 0.5
                spacing 20
                for i in range(battle_controller.player_chips):
                    imagebutton idle "chip.png" action [NullAction()]
            label f"你的行动({battle_controller.player_table_desc}):" xalign 0.5
            hbox:
                spacing 10
                xalign 0.5
                box_wrap True
                xmaximum 1080
                for card in battle_controller.player_table:
                    if isinstance(card,CardSlot):
                        textbutton "":
                            text_size 24
                            xsize 200
                            ysize 284
                            background Frame(card.background,yminimum=57, xminimum=57, yfill=True)
                            action [NullAction()]
                    else:
                        textbutton card.title:
                            style style.common_card
                            text_size 24
                            xsize 200
                            ysize 284
                            background Composite((200,284),
                                            (0,0),Frame(card.background,
                                                            yminimum=57, xminimum=57, yfill=True),
                                            (0,0),Frame(card.inner,
                                                            yminimum=57, xminimum=57))
                            action [Function(battle_controller.player_return_card, card)]
            if battle_controller.is_end():
                textbutton "离开" action [Return()] text_size 40 xalign 0.5
            elif battle_controller.player_table_len()>0:
                textbutton "结束回合" action [Function(battle_controller.end_turn)] text_size 40 xalign 0.5
    frame:
        background None
        ysize 300
        yalign 1.0
        xfill True
        hbox:
            spacing -240
            yalign 0.5
            xalign 0.5
            box_wrap True
            xmaximum 1080

            for i,card in enumerate(battle_controller.player_hand):
                $ pos_i = i-int(len(battle_controller.player_hand)/2)
                $ ypos_value = abs(pow(pos_i,2)*10)-100 - (20 if battle_hovered_card == card else 0)
                textbutton card.title:
                    style style.common_card
                    text_size 24
                    xsize 200
                    ysize 284
                    ypos ypos_value
                    background Composite((200,284),
                                                    (0,0),Frame(card.background,
                                                                    yminimum=57, xminimum=57, yfill=True),
                                                    (0,0),Frame(card.inner,
                                                                    yminimum=57, xminimum=57))
                    hovered [SetVariable("battle_hovered_card",card)]
                    unhovered [SetVariable("battle_hovered_card",None)]
                    action [Function(battle_controller.player_play_card, card)]
                    at card_rotation(pos_i)
    if battle_controller.halftime is not None:
        if battle_controller.halftime.current_card is None:

            use dm_say("中场休息！",battle_controller.halftime.step):
                if battle_controller.halftime.player_win:
                    text "你赢得了本轮，所以接下来将会使用你的卡牌!"
                else:
                    text "你输掉了本轮，所以接下来将会使用敌人的卡牌!"
                text f"本轮的卡牌是{len(battle_controller.halftime.cards)}张，开始使用吧！"
        else:
            frame:
                xfill True
                yfill True
                background Solid("#000c",xfill=True,yfill=True)
                button:
                    xfill True
                    yfill True
                    action [NullAction()]
            frame:
                xfill True
                yalign 0.4
                background None
                vbox:
                    xfill True
                    imagebutton idle battle_controller.halftime.current_card.inner action [NullAction()] xalign 0.5
                    if len(battle_controller.halftime.cards)>0:
                            textbutton "继续" action [Function(battle_controller.halftime.step)] xalign 0.5
                    else:
                            textbutton "结束" action [Function(battle_controller.halftime.end)] xalign 0.5


            frame:
                style_prefix "say"
                xfill True
                yfill True
                background None
                window:
                    id "window"
                    vbox:
                        text "DM" id "who"
                        text f"{battle_controller.halftime.current_card.addition.fantasy}"
                        text f"{{color=#FFC300}}{battle_controller.halftime.current_card.addition.reality}{{/color}}"

    if battle_controller.is_end():
        use dm_say("","Return()"):
            for line in battle_controller.result_display():
                text line

screen battle_reward:
    frame:
        style_prefix "say"
        xfill True
        yfill True
        background Solid("#000c",xfill=True,yfill=True)
        window:
            id "window"
            vbox:
                text "DM" id "who"
                text "你刚刚赢得了一次战斗,选择一个奖励！" id "what"
    frame:
        background None
        xfill True
        yalign 0.4
        hbox:
            spacing 40
            xalign 0.5
            for card in battle_reward_cards:
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
                    action [Function(battle_action_controller.player_get_action,card.addition),SetVariable("battle_reward_cards",None),Return()]
