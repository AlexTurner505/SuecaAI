from tkinter import *
import random
from PIL import Image, ImageTk
from utils import Card, Deck

global deck
deck = Deck()

player1 = []
player2 = []
player3 = []
player4 = []


def resize_cards(card):
    
    card_img = Image.open(card)
    card_img = card_img.resize((150, 218))

    global our_card_image
    our_card_image = ImageTk.PhotoImage(card_img)

    return our_card_image


def shuffle():

    suits = ["diamonds", "hearts", "spades", "clubs"]
    values = list(range(2, 11)) + ["jack", "queen", "king", "ace"]

    for suit in suits:
        for value in values:
            card = Card(suit, value)
            deck.add_card(card)

def deal():

    shuffle()

    for _ in range(10):

        card = random.choice(deck.cards)
        deck.remove_card(card)
        player1.append(card)

        global player1_image
        player1_image = resize_cards(f'./cards/{card.rank}_of_{card.suit}.png')

        player1_label.config(image=player1_image)

        card = random.choice(deck.cards)
        deck.remove_card(card)
        player2.append(card)

        global player2_image
        player2_image = resize_cards(f'./cards/{card.rank}_of_{card.suit}.png')

        player2_label.config(image=player2_image)

        card = random.choice(deck.cards)
        deck.remove_card(card)
        player3.append(card)

        global player3_image
        player3_image = resize_cards(f'./cards/{card.rank}_of_{card.suit}.png')

        player3_label.config(image=player3_image)

        card = random.choice(deck.cards)
        deck.remove_card(card)
        player4.append(card)

        global player4_image
        player4_image = resize_cards(f'./cards/{card.rank}_of_{card.suit}.png')

        player4_label.config(image=player4_image)


root = Tk()
root.title("Sueca Game")
root.geometry("800x600")
root.configure(bg="green")


my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Dealer and Player frames

player1_frame = LabelFrame(my_frame, text="Player 1", bd=0)
player1_frame.grid(row=0, column=0, padx=20, ipadx=20)

player2_frame = LabelFrame(my_frame, text="Player 2", bd=0)
player2_frame.grid(row=0, column=1, ipadx=20)

player3_frame = LabelFrame(my_frame, text="Player 3", bd=0) 
player3_frame.grid(row=0, column=2, padx=20, ipadx=20)

player4_frame = LabelFrame(my_frame, text="Player 4", bd=0)
player4_frame.grid(row=0, column=3, ipadx=20)

#Put cards in frames

player1_label = Label(player1_frame, text="")
player1_label.pack(pady=20)

player2_label = Label(player2_frame, text="")
player2_label.pack(pady=20)

player3_label = Label(player3_frame, text="")
player3_label.pack(pady=20)

player4_label = Label(player4_frame, text="")
player4_label.pack(pady=20)

# Buttons

deal_button = Button(root, text="Deal", font=("Helvetica", 32), command=deal)
deal_button.pack(pady=20)

deal()


root.mainloop()