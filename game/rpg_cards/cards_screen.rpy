screen player_deck:
    frame:
        xfill True
        yfill True
        add "images/deck_bg.png"
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            hbox:
                xfill True
                box_wrap True
                xmaximum 1080
                for card in cards_controller.player_deck():
                    textbutton card.addition.display_text():
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