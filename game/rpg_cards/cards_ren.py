"""renpy
init -100 python:
"""


class Card:
    def __init__(self, number, suit, name, title, description, addition, black=False):
        self.number = number
        self.suit = suit
        self.name = name
        self.title = title
        self.description = description
        self.black = black
        self.background = f'images/card_bg/{"black" if black else "white"}/{suit}_{number}_{"black" if black else "white"}.png'
        self.inner = f'images/inner/{name}.png'
        self.addition = addition


class CardSlot:
    def __init__(self):
        self.card = None
        self.image = 'images/cards/card_slot.png'
        self.background = 'images/cards/card_slot.png'
        self.suit = 'Slot'
        self.number = 0
        self.addition = None


CARD_SLOT = CardSlot()

CARD_SUITS =[
    "Clovers",
    "Hearts",
    "Pikes",
    "Tiles"
]