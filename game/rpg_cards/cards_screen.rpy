default player_deck_cards = []
default player_deck_chosen_card = None
label open_player_deck:
    call screen player_deck
    return

screen player_deck:
    $ player_deck_cards = [ action.card() for action in battle_action_controller.player_deck()]
    frame:
        xfill True
        yfill True
        yalign 0.05
        add "images/deck_bg.png"
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            grid 5 10:
                xfill True
                for card in player_deck_cards:
                    textbutton card.addition.display_text():
                        style style.common_card
                        text_size 24
                        xsize 200
                        ysize 284
                        background Composite((200,284),
                                                        (0,0),Frame(card.background,
                                                                        yminimum=284, xminimum=200, yfill=True),
                                                        (0,0),Frame(card.inner,
                                                                        yminimum=284, xminimum=200))
                        action [SetVariable('player_deck_chosen_card',card)]
    frame:
        background None
        xfill True
        yalign 0.9
        textbutton "离开":
            action [Return()]
            xalign 0.5
    if player_deck_chosen_card is not None:
        button:
            xfill True
            yfill True
            xpos 0
            ypos 0
            action [SetVariable('player_deck_chosen_card',None)]
        frame:
            background Solid("#000c",xfill=True,yfill=True)
            xfill True
            yfill True
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 30
                textbutton player_deck_chosen_card.addition.display_text():
                            style style.common_card
                            text_size 24
                            xsize 200
                            ysize 284
                            background Composite((200,284),
                                                            (0,0),Frame(player_deck_chosen_card.background,
                                                                            yminimum=284, xminimum=200, yfill=True),
                                                            (0,0),Frame(player_deck_chosen_card.inner,
                                                                            yminimum=284, xminimum=200))
                            action [NullAction()]
                hbox:
                    xalign 0.5
                    textbutton "删除":
                        action [Function(battle_action_controller.player_discard_action,player_deck_chosen_card.addition),SetVariable('player_deck_chosen_card',None)]