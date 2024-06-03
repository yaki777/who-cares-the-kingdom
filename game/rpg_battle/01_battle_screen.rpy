default first_battle = True
default card_description = ""
default battle_show_card = None
default battle_chosen_card = None
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
    if first_battle:
        show screen battle_screen
        DM "这是你的第一次战斗，接下来让我为你讲解一下战斗的规则。"
        DM "每个回合你和敌人都会出最多5张卡牌，然后按照德州扑克的规则进行比较。"
        DM "如果你的卡牌点数比敌人小，则你会失去1点MP。当你的MP减少到0时，你失败。"
        DM "无论你或者敌人胜出，你都要完成胜出方使用的卡牌卡面上的任务。"
        DM "每个完成的任务都会减少敌人的HP。当敌人的HP减少到0时，你胜利。"
        DM "规则讲解完了，接下来看你啦！"
        hide screen battle_screen
        $ first_battle = False
    call screen battle_screen
    return

label after_battle_screen:
    $ battle_reward_cards = battle_controller.settle_battle_result()
    if battle_reward_cards is not None:
        call screen battle_reward
    return
screen battle_screen:
    sensitive not first_battle
    frame:
        xfill True
        yfill True
        background Solid("#000a",xfill=True,yfill=True)
        if battle_controller.is_end():
            textbutton "离开" action [Return()] text_size 40 xalign 0.5 yalign 0.6
        else:
            textbutton "结束回合" action [Function(battle_controller.end_turn)] text_size 40 xalign 0.5 yalign 0.7

    use quick_menu
    frame:
        background Composite((940,450),
            (100,0),Frame("images/chat.png",xsize=940,ysize=150),
            (100,130),Frame("images/chat.png",xsize=940,ysize=300),
            (0,300),Frame(Crop((0,0,720,720),battle_controller.enemy.side_image),xsize=160,ysize=160))
        ysize 450
        xfill True
        yalign 0.2
        text f"...\n{{color=#ff084a}}HP:{battle_controller.enemy.hp-battle_controller.player_rank}/{battle_controller.enemy.hp}{{/color}}" xalign 0.2 yalign 0.1 size 24 color "#000"
        hbox:
            yalign 0.7
            xalign 0.55
            for card in battle_controller.enemy_table:
                if isinstance(card, Card):
                    textbutton card.title:
                        style style.common_card
                        text_size 24
                        xsize 160
                        ysize 227
                        background Composite((160,227),
                                        (0,0),Frame(card.background,
                                                        yminimum=57, xminimum=57, yfill=True),
                                        (0,0),Frame(card.inner,
                                                        yminimum=57, xminimum=57))
                        action [SetVariable('battle_show_card',card)]


    frame:
        background Composite((940,450),
            (20,0),Frame("images/chat_me.png",xsize=940,ysize=150),
            (20,130),Frame("images/chat_me.png",xsize=940,ysize=300),
            (920,300),Frame(Crop((0,0,720,720),'images/npc/npc_Aurelia.png'),xsize=160,ysize=160))
        xfill True
        ysize 450
        yalign 0.6
        text f"我想...\n{{color=#005b96}}MP:{battle_controller.player_mp}/{player.mp}{{/color}}" xalign 0.1 yalign 0.1 size 24 color "#000"
        hbox:
            xalign 0.43
            yalign 0.7
            for card in battle_controller.player_table:
                if isinstance(card,Card):
                    textbutton card.title:
                        style style.common_card
                        text_size 24
                        xsize 160
                        ysize 227
                        background Composite((160,227),
                                        (0,0),Frame(card.background,
                                                        yminimum=57, xminimum=57, yfill=True),
                                        (0,0),Frame(card.inner,
                                                        yminimum=57, xminimum=57))
                        action [Function(battle_controller.player_return_card, card)]


    # 手牌
    frame:
        background None
        ysize 300
        yalign 1.0
        xfill True
        hbox:
            spacing -350
            yalign 0.5
            xalign 0.5
            xmaximum 1080

            for i,card in enumerate(battle_controller.player_hand):
                $ pos_i = i-int(len(battle_controller.player_hand)/2)
                $ ypos_value = int(abs(pow(pos_i,2)*8))-100 - (20 if battle_hovered_card == card else 0)
                textbutton card.title:
                    style style.small_card
                    text_size 24
                    xsize 260
                    ysize 370
                    ypos ypos_value
                    background Composite((260,370),
                                                    (0,0),Frame(card.background,
                                                                    yminimum=57, xminimum=57, yfill=True),
                                                    (0,0),Frame(card.inner,
                                                                    yminimum=57, xminimum=57))
                    hovered [SetVariable("battle_hovered_card",card)]
                    action [SetVariable("battle_chosen_card",card)]
                    at card_rotation(pos_i)
    # 放置准备
    if battle_chosen_card is not None:
        frame:
            xfill True
            yfill True
            background None
            button:
                xfill True
                yfill True
                xpos 0
                ypos 0
                action [SetVariable("battle_chosen_card", None)]
        frame:
            background None
            yalign 0.5
            xalign 0.5
            vbox:
                xalign 0.5
                yalign 0.5
                textbutton battle_chosen_card.title:
                    style style.common_card
                    text_size 32
                    xsize 400
                    ysize 568
                    background Composite((400,568),
                        (0,0),Frame(battle_chosen_card.background,
                                        yminimum=57, xminimum=57, yfill=True),
                        (0,0),Frame(battle_chosen_card.inner,
                                        yminimum=57, xminimum=57, yfill=True))
                    action [Function(battle_controller.player_play_card, battle_chosen_card), SetVariable("battle_chosen_card", None)]
                textbutton "放置":
                    style style.common_card
                    xalign 0.5
                    action [Function(battle_controller.player_play_card, battle_chosen_card), SetVariable("battle_chosen_card", None)]
    # 展示卡牌
    if battle_show_card is not None:
        frame:
            xfill True
            yfill True
            background None
            button:
                xfill True
                yfill True
                xpos 0
                ypos 0
                action [SetVariable("battle_show_card", None)]
        frame:
            background None
            yalign 0.5
            xalign 0.5
            vbox:
                xalign 0.5
                yalign 0.5
                textbutton battle_show_card.title:
                    style style.common_card
                    text_size 32
                    xsize 400
                    ysize 568
                    background Composite((400,568),
                        (0,0),Frame(battle_show_card.background,
                                        yminimum=57, xminimum=57, yfill=True),
                        (0,0),Frame(battle_show_card.inner,
                                        yminimum=57, xminimum=57, yfill=True))
                    action [Function(SetVariable("battle_show_card", None))]

    if battle_controller.is_end():
        use dm_say("","Return()"):
            for line in battle_controller.result_display():
                text line
    # 中场休息
    if battle_controller.halftime is not None:
        if battle_controller.halftime.current_card is None:
            if battle_controller.halftime.is_end:
                use dm_say("休息结束！",battle_controller.halftime.end)
            else:
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
                    spacing 30
                    xfill True
                    imagebutton idle battle_controller.halftime.current_card.addition.image action [NullAction()] xalign 0.5

                    text f"{battle_controller.halftime.current_card.addition.fantasy}" size 28
                    text "{color=#ff8b94}任务:{/color}"
                    text f"{{color=#FFC300}}{battle_controller.halftime.current_card.addition.reality}{{/color}}" size 28
                    hbox:
                        xalign 0.5
                        spacing 50
                        textbutton "{color=#88d8b0}完成{/color}" action [Function(battle_controller.halftime.step,True)] text_size 40
                        textbutton "{color=#ff6f69}失败{/color}" action [Function(battle_controller.halftime.step,False)] text_size 40

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
        vbox:
            xalign 0.5
            spacing 40
            hbox:
                spacing 40
                xalign 0.5
                for card in battle_reward_cards:
                    textbutton card.title:
                        style style.common_card
                        text_size 24
                        xsize 260
                        ysize 370
                        background Composite((260,370),
                            (0,0),Frame(card.background,
                                            yminimum=57, xminimum=57, yfill=True),
                            (0,0),Frame(card.inner,
                                            yminimum=57, xminimum=57, yfill=True))
                        action [Function(battle_action_controller.player_get_action,card.addition),SetVariable("battle_reward_cards",None),Return()]
            textbutton "跳过":
                xalign 0.5
                action [SetVariable("battle_reward_cards",None),Return()]
