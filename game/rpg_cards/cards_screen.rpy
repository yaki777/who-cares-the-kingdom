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
        textbutton "{color=#dcedc1}离开{/color}":
            action [Return()]
            xalign 0.5
    if player_deck_chosen_card is not None:
        button:
            background Solid("#000c",xfill=True,yfill=True)

            xfill True
            yfill True
            xpos 0
            ypos 0
            action [SetVariable('player_deck_chosen_card',None)]
        frame:
            xfill True
            yfill True
            background None
            vbox:
                spacing 30
                xfill True
                yalign 0.4
                textbutton player_deck_chosen_card.title:
                    xalign 0.5
                    style style.common_card
                    text_size 24
                    xsize 400
                    ysize 568
                    background Composite((400,568),
                        (0,0),Frame(player_deck_chosen_card.background,
                                        yminimum=57, xminimum=57, yfill=True),
                        (0,0),Frame(player_deck_chosen_card.inner,
                                        yminimum=57, xminimum=57, yfill=True))
                    action [NullAction()]

                vbox:
                    xalign 0.5
                    spacing 10
                    text f"{player_deck_chosen_card.addition.title}"
                    text f"{{color=#ffd3b6}}{CARD_SUIT_DICT[player_deck_chosen_card.suit]}{player_deck_chosen_card.number}{{/color}}" size 30

                    text f"[[主题:{player_deck_chosen_card.addition.theme},类别:{','.join(player_deck_chosen_card.addition.tags)}]" size 30
                    text "{color=#ff8b94}任务:{/color}"
                    text f"{{color=#FFC300}}{player_deck_chosen_card.addition.reality}{{/color}}" size 28
            hbox:
                yalign 0.9
                xalign 0.5
                spacing 50
                textbutton "{color=#ff6f69}删除{/color}":
                    action [Function(battle_action_controller.player_discard_action,player_deck_chosen_card.addition),SetVariable('player_deck_chosen_card',None)]