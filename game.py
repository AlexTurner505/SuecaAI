from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title("Sueca Game")
root.geometry("800x600")
root.configure(bg="green")

def resize_cards(card):
    
    card_img = Image.open(card)
    card_img = card_img.resize((150, 218))

    global our_card_image
    our_card_image = ImageTk.PhotoImage(card_img)

    return our_card_image

def shuffle():
    suits = ["diamonds", "hearts", "spades", "clubs"]
    values = list(range(2, 11)) + ["jack", "queen", "king", "ace"]

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    global dealer, player

    dealer = []
    player = []

    card = random.choice(deck)
    deck.remove(card)
    dealer.append(card)

    global dealer_image
    dealer_image = resize_cards(f'./cards/{card}.png')

    dealer_label.config(image=dealer_image)

    card = random.choice(deck)
    deck.remove(card)
    player.append(card)

    global player_image
    player_image = resize_cards(f'./cards/{card}.png')

    player_label.config(image=player_image)


def deal_cards():
    try:
        card = random.choice(deck)
        deck.remove(card)
        dealer.append(card)

        global dealer_image
        dealer_image = resize_cards(f'./cards/{card}.png')

        dealer_label.config(image=dealer_image)

        card = random.choice(deck)
        deck.remove(card)
        player.append(card)

        global player_image
        player_image = resize_cards(f'./cards/{card}.png')

        player_label.config(image=player_image)
         
    except:
        root.title("Error! No cards to deal")

my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Dealer and Player frames

dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

#Put cards in frames

dealer_label = Label(dealer_frame, text="")
dealer_label.pack(pady=20)

player_label = Label(player_frame, text="")
player_label.pack(pady=20)

# Buttons

shuffle_button = Button(root, text="Shuffle", font=("Helvetica", 32), command=shuffle)
shuffle_button.pack(pady=20)

deal_button = Button(root, text="Deal", font=("Helvetica", 32), command=deal_cards)
deal_button.pack(pady=20)

shuffle()

root.mainloop()