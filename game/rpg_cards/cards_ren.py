from rpg_cards.card_actions_ren import CA_MASTURBATE

"""renpy
init -100 python:
"""

DRAW_TYPE_NORMAL = 0
DRAW_TYPE_FIRST_TURN = 1
DRAW_TYPE_EVERY_TURN = 2


class Card:
    def __init__(self, number, suit, name, title, description, addition, black=False):
        self.number = number
        self.suit = suit
        self.name = name
        self.title = title
        self.description = description
        self.black = black
        self.image = f'images/card_bg/{"black" if black else "white"}/{suit}_{number}_{name}.png'
        self.background = f'images/card_bg/{"black" if black else "white"}/{suit}_{number}_{"black" if black else "white"}.png'
        self.inner = f'images/inner/{name}.png'
        self.addition = addition
        self.draw_type = DRAW_TYPE_NORMAL

    def copy(self):
        return Card(self.name, self.title, self.description)


class CardSlot:
    def __init__(self):
        self.card = None
        self.image = 'images/cards/card_slot.png'
        self.background = 'images/cards/card_slot.png'
        self.suit = 'Slot'
        self.number = 0


CARD_SLOT = CardSlot()

CARD_LIBRARY = [
    Card(8, "Pikes", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(4, "Hearts", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(10, "Pikes", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(14, "Clovers", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(2, "Clovers", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(6, "Heats", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(5, "Clovers", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(12, "Hearts", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(3, "Hearts", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(13, "Clovers", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(9, "Hearts", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(10, "Clovers", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(2, "Tiles", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(11, "Hearts", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(10, "Hearts", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(8, "Clovers", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(4, "Tiles", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(2, "Hearts", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(4, "Clovers", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(8, "Tiles", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(9, "Tiles", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(3, "Clovers", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(7, "Tiles", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(7, "Clovers", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(13, "Hearts", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(12, "Clovers", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(9, "Clovers", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(11, "Clovers", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(12, "Pikes", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(11, "Tiles", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(3, "Pikes", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(14, "Tiles", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(12, "Tiles", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(14, "Pikes", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(13, "Tiles", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(5, "Hearts", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(9, "Pikes", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(7, "Pikes", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(5, "Tiles", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(14, "Hearts", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(11, "Pikes", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(6, "Tiles", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(3, "Tiles", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(5, "Pikes", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(2, "Pikes", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(7, "Hearts", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(4, "Pikes", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(8, "Hearts", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(6, "Clovers", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(10, "Tiles", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(13, "Pikes", "action1", "Test Card", "This is a test card.", CA_MASTURBATE),
    Card(6, "Pikes", "action1", "Test Card", "This is a test card.", CA_MASTURBATE)
]
