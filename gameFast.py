from tkinter import *
import random
from utils import *
import math
import time

class SuecaGameText:
    def __init__(self, root):
        self.deck = Deck()
        self.player1 = []
        self.player2 = []
        self.player3 = []
        self.player4 = []
        self.played_cards = []
        self.round_cards = []
        self.score1 = 0
        self.score2 = 0
        self.starting_player = 1
        self.current_player = 1
        self.turn = 1
        self.starting_round_player = self.starting_player
        self.starting_round_suit = None
        self.games = 100

    def __str__(self):
        game_details = "Game Details:\n"
        game_details += f"Player 1 Hand: {[str(card) for card in self.player1]}\n"
        game_details += f"Player 2 Hand: {[str(card) for card in self.player2]}\n"
        game_details += f"Player 3 Hand: {[str(card) for card in self.player3]}\n"
        game_details += f"Player 4 Hand: {[str(card) for card in self.player4]}\n"
        game_details += f"Round Cards: {self.round_cards}\n"
        game_details += f"Played Cards: {self.played_cards}\n"
        game_details += f"Score: Team 1 - {self.score1}, Team 2 - {self.score2}\n"
        game_details += f"Starting Player: {self.starting_player}\n"
        game_details += f"Current Player: {self.current_player}\n"
        game_details += f"Turn: {self.turn}\n"
        game_details += f"Starting Round Player: {self.starting_round_player}\n"
        game_details += f"Starting Round Suit: {self.starting_round_suit}\n"
        return game_details


    def main_game_loop(self):
        a = 10
        while (True):
            if (self.player1 == [] and self.player2 == [] and self.player3 == [] and self.player4 == []):
                self.starting_player = (self.starting_player % 4) + 1
                print(f"Score: Team 1 - {self.score1}, Team 2 - {self.score2}")
                self.games -= 1
                if self.games == 0:
                    break    
                self.deal()
                
                

            if self.turn < 4:
                self.card_random()
            elif self.turn == 4:
                self.card_random()
                self.update_scoreboard()
                self.round_cards = []
                self.turn = 1

    def update_scoreboard(self):
        total_points = sum(tuple_[0].points for tuple_ in self.round_cards)


        if any(card.suit == self.deck.trump.suit for card, _ in self.round_cards):
            max_card = max(self.round_cards, key=lambda tuple_: tuple_[0].points if tuple_[0].suit == self.deck.trump.suit else 0)
        else:
            max_card = max(self.round_cards, key=lambda tuple_: tuple_[0].points if tuple_[0].suit == self.starting_round_suit else 0)

        winning_team = max_card[1]    
            
        if winning_team == 1:
            self.score1 += total_points
        else:
            self.score2 += total_points


    def start_deck(self):
        suits = ["diamonds", "hearts", "spades", "clubs"]
        values = list(range(2, 8)) + ["jack", "queen", "king", "ace"]

        for suit in suits:
            for value in values:
                card = Card(suit, value)
                self.deck.add_card(card)

    def deal(self):

        self.start_deck()

        self.score1, self.score2 = 0, 0
        self.starting_round_suit = None
        self.turn = 1

        self.current_player = self.starting_player
        self.starting_round_player = self.starting_player

        self.player1.clear()
        self.player2.clear()
        self.player3.clear()
        self.player4.clear()

        self.round_cards = []

        self.played_cards.clear()

        players = [self.player1, self.player2, self.player3, self.player4]

        players = players[self.starting_player-1:] + players[:self.starting_player-1]

        first_card = True

        for player in players:
            for _ in range(10):
                card = random.choice(self.deck.cards)
                self.deck.remove_card(card)
                player.append(card)
                if first_card:
                    self.deck.add_trump(card)
                    first_card = False 

    def card_selected(self, card, index):
        # Card selection code here
        pass

    def card_random(self):

        if self.current_player == 1:
            player_cards = self.player1
        elif self.current_player == 2:
            player_cards = self.player2
        elif self.current_player == 3:
            player_cards = self.player3
        elif self.current_player == 4:
            player_cards = self.player4

        if self.starting_round_player == self.current_player:
            valid_cards = player_cards
            card = random.choice(valid_cards)
            self.starting_round_suit = card.suit

        else:
            has_starting_round_suit = any(card.suit == self.starting_round_suit for card in player_cards)

            if has_starting_round_suit:
                valid_cards = [card for card in player_cards if card.suit == self.starting_round_suit]
            else:
                valid_cards = player_cards

            card = random.choice(valid_cards)

        if self.current_player == 1:
            self.round_cards.append((card, 1))
            self.player1.remove(card)
            self.current_player = 2
        elif self.current_player == 2:
            self.round_cards.append((card, 2))
            self.player2.remove(card)
            self.current_player = 3
        elif self.current_player == 3:
            self.round_cards.append((card, 1))
            self.player3.remove(card)
            self.current_player = 4
        elif self.current_player == 4:
            self.round_cards.append((card, 2))
            self.player4.remove(card)
            self.current_player = 1

        self.played_cards.append(card)
        self.turn += 1

root = Tk()
game = SuecaGameText(root)
game.deal()
print(game)
game.main_game_loop()
print(game)
