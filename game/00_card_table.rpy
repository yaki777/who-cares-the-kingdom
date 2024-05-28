style common_card is button:
    xpadding 15 # plus other stuff if you want (for more control remove the ' is button' bit)
style small_card is button:
    xpadding 15 # plus other stuff if you want (for more control remove the ' is button' bit)

style small_card_text: # optionally ... is button_text:
    yalign 0.93
    xalign 0.1
    color "#FFF"
    outlines [ (0.5, "#333", 0, 0) ]
    yfill True

style common_card_text: # optionally ... is button_text:
    yalign 0.94
    xalign 0.5
    text_align 0.5
    color "#FFF"
    outlines [ (0.5, "#333", 0, 0) ]
    yfill True

transform card_rotation(index):
    rotate int(10*index)
default card_table_chosen_card = None
default card_table_hovered_card = None
screen card_table(table_bg,placed_card,player_hands,place_card_callback):

    frame:
        add table_bg
        xfill True
    frame:
        background None
        yalign 0.05
        hbox:
            spacing 30
            imagebutton idle Frame("gui/plate_box.png"):
                xsize 100
                ysize 100
                action [Call('open_player_deck')]

            imagebutton idle Frame("gui/journal.png"):
                xsize 100
                ysize 100
                action [NullAction()]

    frame:
        background None
        ysize 300
        xalign 0.5
        yalign 0.7
        if placed_card is not None:
            textbutton placed_card.title:
                style style.common_card
                text_size 24
                xsize 200
                ysize 284

                background Composite((200,284),
                    (0,0),Frame(placed_card.background,
                                    yminimum=57, xminimum=57, yfill=True),
                    (0,0),Frame(placed_card.inner,
                                    yminimum=57, xminimum=57, yfill=True))
                action [SetVariable("card_table_chosen_card", None)]
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
            spacing -260
            $ hands_len = len(player_hands)-1
            for i,card in enumerate(player_hands):

                $ pos_i = i-hands_len/2
                $ ypos_value = int(abs(pow(pos_i,2)*8))-100 - (20 if card_table_hovered_card == card else 0)
                textbutton card.title:
                    style style.small_card
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
                    action [SetVariable("card_table_chosen_card", card)]
                    hovered [SetVariable("card_table_hovered_card",card)]
                    unhovered [SetVariable("card_table_hovered_card",None)]
                    at card_rotation(pos_i)
    frame:
        background None
        yalign 0.68
        xalign 0.5
        if card_table_chosen_card is not None:
            vbox:
                xalign 0.5
                yalign 0.5
                textbutton card_table_chosen_card.title:
                    style style.common_card
                    text_size 24
                    xsize 400
                    ysize 568
                    background Composite((400,568),
                        (0,0),Frame(card_table_chosen_card.background,
                                        yminimum=57, xminimum=57, yfill=True),
                        (0,0),Frame(card_table_chosen_card.inner,
                                        yminimum=57, xminimum=57, yfill=True))
                    action [Function(place_card_callback, card_table_chosen_card), SetVariable("card_table_chosen_card", None)]
                textbutton "放置" xalign 0.5 action [Function(place_card_callback, card_table_chosen_card), SetVariable("card_table_chosen_card", None)]
    use quick_menu


screen dm_say(what,next_callback=None):
    button:
        xfill True
        yfill True
        xpos 0
        ypos 0
        if not isinstance(next_callback,str):
            action [Function(next_callback)]
        elif next_callback == "Return()":
            action [Return()]
    frame:
        style_prefix "say"
        xfill True
        yfill True
        background Solid("#000c",xfill=True,yfill=True)
        window:
            id "window"
            vbox:
                text "DM" id "who"
                text what id "what"
                transclude