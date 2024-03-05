from tkinter import *
import random
from PIL import Image, ImageTk
from utils import *
import math
import time

global deck
deck = Deck()

player1 = []
player2 = []
player3 = []
player4 = []


global player1_images, player2_images, player3_images, player4_images
player1_images = []
player2_images = []
player3_images = []
player4_images = []


def main_game_loop():
    
    
    global current_player
    
    if current_player == 1:
        print("Player 1's turn")
        # Implement player 1's turn logic here
    elif current_player == 2:
        print("Player 2's turn")

        card = random.choice(player2)

        player2_card_label.config(image=player2_images[player2.index(card)])

        player2.remove(card)

        current_player = 3
    elif current_player == 3:
        print("Player 3's turn")
        
        card = random.choice(player3)

        player3_card_label.config(image=player3_images[player3.index(card)])

        player3.remove(card)

        current_player = 4
    elif current_player == 4:
        print("Player 4's turn")
        
        card = random.choice(player4)

        player4_card_label.config(image=player4_images[player4.index(card)])

        player4.remove(card)

        current_player = 1

    # Schedule the next iteration of the main loop after a delay
    # You can adjust the delay based on your game's requirements
    root.after(2000, main_game_loop)

    # Check for end game conditions and update UI accordingly




def start_deck():

    suits = ["diamonds", "hearts", "spades", "clubs"]
    values = list(range(2, 8)) + ["jack", "queen", "king", "ace"]

    for suit in suits:
        for value in values:
            card = Card(suit, value)
            deck.add_card(card)

def deal():

    start_deck()

    player1.clear()
    player2.clear()
    player3.clear()
    player4.clear()

    player1_images.clear()
    player2_images.clear()
    player3_images.clear()
    player4_images.clear()

    for i in range(10):

        card = random.choice(deck.cards)
        deck.remove_card(card)
        player1.append(card)

        player1_images.append(resize_cards(f'./cards/{card.rank}_of_{card.suit}.png'))

        player1_labels[i].config(image=player1_images[i])
        player1_labels[i].bind("<Button-1>", lambda event, index=i: card_selected(index))

        card = random.choice(deck.cards)
        deck.remove_card(card)
        player2.append(card)

        player2_images.append(resize_cards(f'./cards/{card.rank}_of_{card.suit}.png'))

        card = random.choice(deck.cards)
        deck.remove_card(card)
        player3.append(card)

        player3_images.append(resize_cards(f'./cards/{card.rank}_of_{card.suit}.png'))

        card = random.choice(deck.cards)
        deck.remove_card(card)
        player4.append(card)

        player4_images.append(resize_cards(f'./cards/{card.rank}_of_{card.suit}.png'))

        
def card_selected(index):
    global current_player
    if (current_player == 1):
        player1_card_label.config(image=player1_images[index])
        current_player = 2

root = Tk()
root.title("Sueca Game")
root.geometry("800x600")
root.configure(bg="green")

def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

root.bind("<Escape>", toggle_fullscreen)



# Dealer and Player frames

player1_frame = LabelFrame(root, bg="brown")
player1_frame.pack(side=BOTTOM, padx=10, pady=20)

player2_frame = LabelFrame(root, bd=0, bg="white")
player2_frame.place(x=1400, y=100)

player3_frame = LabelFrame(root, bd=0, bg="white") 
player3_frame.pack(side=TOP, padx=10, pady=20)

player4_frame = LabelFrame(root, bd=0, bg="white")
player4_frame.place(x=40, y=100)

tabel_frame = LabelFrame(root, bd=0, bg="brown", highlightbackground="white", highlightthickness=2)
tabel_frame.place(x=400, y=200, height=400, width=750)

#Put cards in frames

player1_labels = []

for i in range(10):
    label = Label(player1_frame, text="", bg="brown")
    label.grid(row=0, column=i, pady=5, padx=5)
    player1_labels.append(label)

player2_label = Label(player2_frame, text="Player 2", bg="white", width=13, height=8)
player2_label.grid(row=0, column=0)

player3_label = Label(player3_frame, text="Player 3", bg="white", width=13, height=8)
player3_label.grid(row=0, column=0)

player4_label = Label(player4_frame, text="Player 4", bg="white", width=13, height=8)
player4_label.grid(row=0, column=0)

## Card Labels

player1_card_label = Label(tabel_frame, text="CARD")
player1_card_label.pack(side=BOTTOM, pady=(0, 20))  # Adjusted padding here

player2_card_label = Label(tabel_frame, text="CARD")
player2_card_label.pack(side=RIGHT, padx=10)

player3_card_label = Label(tabel_frame, text="CARD")
player3_card_label.pack(side=TOP, pady=(20, 0))  # Adjusted padding here

player4_card_label = Label(tabel_frame, text="CARD")
player4_card_label.pack(side=LEFT, padx=10)

## Game Logic

current_player = 1

deal()

main_game_loop()


root.mainloop()