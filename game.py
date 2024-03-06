from tkinter import *
import random
from PIL import Image, ImageTk
from utils import *
import math
import time

# Define global variables
global deck, player1, player2, player3, player4, player1_images, player2_images, player3_images, player4_images, starting_player, played_cards, back_card, round_cards, score1, score2

# Initialize deck and player lists
deck = Deck()
player1 = []
player2 = []
player3 = []
player4 = []
player1_labels = []
played_cards = []
round_cards = []

score1 = 0
score2 = 0

starting_player = 1
starting_round_player = starting_player
starting_round_suit = None

# Game Logic
turn = 1

def main_game_loop():
    global current_player, turn, round_cards, starting_player

    if turn <= 4:
        if current_player == 1:
            pass
        else:
            card_random()
            
    else:
        update_scoreboard()
        round_cards = []
        player1_card_label.config(image='')
        player2_card_label.config(image='')
        player3_card_label.config(image='')
        player4_card_label.config(image='')
        turn = 1

    if (player1 == [] and player2 == [] and player3 == [] and player4 == []):
        starting_player = (starting_player % 4) + 1
        deal()

    # Schedule the next iteration of the main loop after a delay
    # You can adjust the delay based on your game's requirements
    root.after(500, main_game_loop)

    # Check for end game conditions and update UI accordingly

def update_scoreboard():
    global score1, score2

    total_points = sum(tuple_[0].points for tuple_ in round_cards)


    if any(card.suit == deck.trump.suit for card, _ in round_cards):
        max_card = max(round_cards, key=lambda tuple_: tuple_[0].points if tuple_[0].suit == deck.trump.suit else 0)
    else:
        max_card = max(round_cards, key=lambda tuple_: tuple_[0].points if tuple_[0].suit == starting_round_suit else 0)

    winning_team = max_card[1]    
        
    if winning_team == 1:
        score1 += total_points
    else:
        score2 += total_points

    update_scoreboard_labels()

def update_scoreboard_labels():
    score1_label.config(text=f"Team 1: {score1}")
    score2_label.config(text=f"Team 2: {score2}")

def start_deck():
    suits = ["diamonds", "hearts", "spades", "clubs"]
    values = list(range(2, 8)) + ["jack", "queen", "king", "ace"]

    global back_card
    back_card = Card("back", "back", resize_cards(f'./cards/back_card.png'))

    for suit in suits:
        for value in values:
            card_image = resize_cards(f'./cards/{value}_of_{suit}.png')
            card = Card(suit, value, card_image)
            deck.add_card(card)

def deal():
    global player1_labels, current_player, starting_player, back_card, score1, score2, starting_round_player, turn, starting_round_suit, round_cards

    start_deck()

    score1 = 0
    score2 = 0
    starting_round_suit = None
    turn = 1

    update_scoreboard_labels()

    current_player = starting_player
    starting_round_player = starting_player

    for label in player1_labels:
        label.destroy()

    create_player_labels()

    player1.clear()
    player2.clear()
    player3.clear()
    player4.clear()

    round_cards = []

    played_cards.clear()

    players = [player1, player2, player3, player4]

    players = players[starting_player-1:] + players[:starting_player-1]

    first_card = True

    for player in players:
        for i in range(10):
            card = random.choice(deck.cards)
            
            deck.remove_card(card)
            player.append(card)
            if first_card:
                deck.add_trump(card)

                if starting_player == 1:
                    pass
                    player1_trump_label.config(image=card.image)
                    player2_trump_label.config(image=back_card.image)
                    player3_trump_label.config(image=back_card.image)
                    player4_trump_label.config(image=back_card.image)
                elif starting_player == 2:
                    player1_trump_label.config(image=back_card.image)
                    player2_trump_label.config(image=card.image)
                    player3_trump_label.config(image=back_card.image)
                    player4_trump_label.config(image=back_card.image)
                elif starting_player == 3:
                    player1_trump_label.config(image=back_card.image)
                    player2_trump_label.config(image=back_card.image)
                    player3_trump_label.config(image=card.image)
                    player4_trump_label.config(image=back_card.image)
                else:
                    player1_trump_label.config(image=back_card.image)
                    player2_trump_label.config(image=back_card.image)
                    player3_trump_label.config(image=back_card.image)
                    player4_trump_label.config(image=card.image)

                first_card = False 
            if player == player1:
                player1_labels[i].config(image=card.image)
                player1_labels[i].bind("<Button-1>", lambda event, index=i, card=card: card_selected(card, index))
   

def card_selected(card, index):
    global current_player, turn, played_cards, starting_round_suit, starting_round_player

    if current_player == 1 and turn <= 4:
        if starting_round_player == 1:
            starting_round_suit = card.suit
        elif starting_round_suit != card.suit:
            
            has_starting_round_suit = any(c.suit == starting_round_suit for c in player1)
            
            if has_starting_round_suit:
                return
            else:
                pass

        player1_card_label.config(image=card.image)
        played_cards.append(card)
        round_cards.append((card, 1))
        player1.remove(card)
        player1_labels[index].destroy()
        current_player = 2
        turn += 1

def card_random():
    global current_player, turn, played_cards, starting_round_suit, starting_round_player

    # Define the player's card list based on the current player
    if current_player == 2:
        player_cards = player2
    elif current_player == 3:
        player_cards = player3
    elif current_player == 4:
        player_cards = player4

    if starting_round_player == current_player:
        valid_cards = player_cards

        card = random.choice(valid_cards)

        starting_round_suit = card.suit

    else:

        # Check if the player has a card of the starting round suit
        has_starting_round_suit = any(card.suit == starting_round_suit for card in player_cards)

        # If the player has a card of the starting round suit, select randomly from those cards
        # Otherwise, allow the player to play any card
        if has_starting_round_suit:
            valid_cards = [card for card in player_cards if card.suit == starting_round_suit]
        else:
            valid_cards = player_cards

        # Select a random card from the valid cards
        card = random.choice(valid_cards)

    # Update the played card label and other variables accordingly
    if current_player == 2:
        player2_card_label.config(image=card.image)
        round_cards.append((card, 2))
        player2.remove(card)
        current_player = 3
    elif current_player == 3:
        player3_card_label.config(image=card.image)
        round_cards.append((card, 1))
        player3.remove(card)
        current_player = 4
    elif current_player == 4:
        player4_card_label.config(image=card.image)
        round_cards.append((card, 2))
        player4.remove(card)
        current_player = 1

    played_cards.append(card)
    turn += 1


root = Tk()
root.title("Sueca Game")
root.geometry("800x600")
root.configure(bg="green")

# Dealer and Player frames
player1_frame = LabelFrame(root, bg="brown")
player1_frame.pack(side=BOTTOM, padx=10, pady=20)

player1_trump_frame = LabelFrame(root, bd=0, bg="white")
player1_trump_frame.place(x=100, y=650)

player2_frame = LabelFrame(root, bd=0, bg="white")
player2_frame.place(x=1400, y=100)

player3_frame = LabelFrame(root, bd=0, bg="white")
player3_frame.pack(side=TOP, padx=10, pady=20)

player4_frame = LabelFrame(root, bd=0, bg="white")
player4_frame.place(x=40, y=100)

tabel_frame = LabelFrame(root, bd=0, bg="brown", highlightbackground="white", highlightthickness=2)
tabel_frame.place(x=400, y=200, height=400, width=750)

scoreboard_frame = LabelFrame(root, bd=0, bg="black",  highlightbackground="white", highlightthickness=2)
scoreboard_frame.place(x=1300, y=670, height=200, width=300)

# Put cards in frames
def create_player_labels():
    global player1_labels, player2_trump_label, player3_trump_label, player4_trump_label, player1_trump_label

    player1_labels = []

    for i in range(10):
        label = Label(player1_frame, text="", bg="brown")
        label.grid(row=0, column=i, pady=5, padx=5)
        player1_labels.append(label)

    player1_trump_label = Label(player1_trump_frame, bg="white")
    player1_trump_label.grid(row=0, column=0)

    player2_trump_label = Label(player2_frame, bg="white")
    player2_trump_label.grid(row=0, column=0)

    player3_trump_label = Label(player3_frame, bg="white")
    player3_trump_label.grid(row=0, column=0)

    player4_trump_label = Label(player4_frame, bg="white")
    player4_trump_label.grid(row=0, column=0)

# Card Labels
player1_card_label = Label(tabel_frame, bg="brown")
player1_card_label.place(x=330, y=240)

player2_card_label = Label(tabel_frame, bg="brown")
player2_card_label.place(x=430, y=140)

player3_card_label = Label(tabel_frame, bg="brown")
player3_card_label.place(x=330, y=40)

player4_card_label = Label(tabel_frame, bg="brown")
player4_card_label.place(x=230, y=140)

# Scoreboard Labels

score1_label = Label(scoreboard_frame, text=f"Team 1: {score1}", bg="black", fg="white", font=("Arial", 20), padx=10, pady=10)
score1_label.grid(row=0, column=0)

score2_label = Label(scoreboard_frame, text=f"Team 2: {score2}", bg="black", fg="white", font=("Arial", 20), padx=10, pady=10)
score2_label.grid(row=1, column=0)


# Game Logic
deal()
main_game_loop()

root.mainloop()
