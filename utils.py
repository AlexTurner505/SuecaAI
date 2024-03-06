import random
from PIL import Image, ImageTk

class Card:
    def __init__(self, suit, rank, image):
        self.suit = suit
        self.rank = rank
        self.image = image

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def add_trump(self, card):
        self.trump = card

    def remove_card(self, card):
        self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)
    

def resize_cards(card):
    
    #105 153
    card_img = Image.open(card)
    card_img = card_img.resize((75, 109))

    global our_card_image
    our_card_image = ImageTk.PhotoImage(card_img)

    return our_card_image