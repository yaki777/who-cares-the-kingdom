default npc_card_description = ""
default hovered_card = -1
default chosen_npc = None
screen dungeon_walk:

    frame:
        add dungeon_controller.current_area.background
        xfill True

    frame:
        background None
        ysize 300
        xalign 0.5
        yalign 0.7
        if dungeon_controller.placed_card is not None:
            textbutton dungeon_controller.placed_card.title:
                style style.common_card
                text_size 24
                xsize 200
                ysize 284

                background Composite((200,284),
                    (0,0),Frame(dungeon_controller.placed_card.background,
                                    yminimum=57, xminimum=57, yfill=True),
                    (0,0),Frame(dungeon_controller.placed_card.inner,
                                    yminimum=57, xminimum=57, yfill=True))
                action [SetVariable("dungeon_chosen_card", None)]
        else:
            textbutton "卡槽":
                style style.common_card
                text_size 24
                xsize 200
                ysize 284

                background Frame( "images/cards/card_slot.png",
                                    yminimum=57, xminimum=57, yfill=True)
                action [NullAction()]
    # 手牌
    frame:
        background None
        ysize 300
        xfill True
        yalign 1.0
        hbox:
            yalign 0.5
            xalign 0.5
            spacing -240
            box_wrap True
            xmaximum 1080
            for i,card in enumerate(dungeon_controller.player_hands):
                $ pos_i = i-int(len(dungeon_controller.player_hands)/2)
                $ ypos_value = abs(pow(pos_i,2)*10)-100 - (20 if dungeon_hovered_card == card else 0)
                textbutton card.title:
                    style style.common_card
                    text_size 24
                    xsize 200
                    ysize 284
                    ypos ypos_value
                    size_group "inv_buttons" # name not important, just makes all with same name same width
                    background Composite((200,284),
                        (0,0),Frame(card.background,
                                        yminimum=57, xminimum=57, yfill=True),
                        (0,0),Frame(card.inner,
                                        yminimum=57, xminimum=57, yfill=True))
                    action [SetVariable("dungeon_chosen_card", card)]
                    hovered [SetVariable("dungeon_hovered_card",card)]
                    unhovered [SetVariable("dungeon_hovered_card",None)]
                    at card_rotation(pos_i)
    frame:
        background None
        yalign 0.68
        xalign 0.5
        if dungeon_chosen_card is not None:
            vbox:
                xalign 0.5
                yalign 0.5
                textbutton dungeon_chosen_card.title:
                    style style.common_card
                    text_size 24
                    xsize 400
                    ysize 568
                    background Composite((400,568),
                        (0,0),Frame(dungeon_chosen_card.background,
                                        yminimum=57, xminimum=57, yfill=True),
                        (0,0),Frame(dungeon_chosen_card.inner,
                                        yminimum=57, xminimum=57, yfill=True))
                    action [NullAction()]
                textbutton "放置" xalign 0.5 action [Function(dungeon_controller.player_place_card, dungeon_chosen_card), SetVariable("dungeon_chosen_card", None)]
