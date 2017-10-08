#!/usr/bin/env python3
# coding=utf-8

from constant.action import Action
from player import Player
from util import graphic_util


class HumanPlayer(Player):
    def __init__(self, hero, deck_cards):
        Player.__init__(self, hero, deck_cards)

    def choose_action(self):
        print("Choose Action:")
        print("1. Attack")
        print("2. Play Card")
        print("3. Pass Turn")
        action = input("Your choice [1/2/3] ")
        return Action(int(action))

    def act_attack(self):
        graphic_util.print_table(self, self.engine.opponent_player())

    def act_play_card(self):
        print("Table Cards")
        graphic_util.print_table(self, self.engine.opponent_player())
        print("Hand Cards")
        graphic_util.print_hand_cards(self)
        while True:
            card_idx = input("Choose your hand card to play: ")
            if not (card_idx.isdigit() or int(card_idx) < 0 or int(card_idx) >= len(self.hand_cards)):
                print("Please choose correct hand card")
                continue
            card_to_play = self.hand_cards[int(card_idx)]
            self.remove_hand_card(card_to_play)
            break

        while True:
            place_idx = input("Choose place to play")
            if not (place_idx.isdigit() or int(place_idx) < -1 or int(place_idx) > len(self.table_cards)):
                print("Please choose correct place")
                continue
            self.add_table_card(card_to_play, int(place_idx))
            break

        print("Table Cards Now!")
        graphic_util.print_table(self, self.engine.opponent_player())
        print("Hand Cards Now!")
        graphic_util.print_hand_cards(self)

    def play_card(self):
        return None

    def add_deck_card(self, card):
        pass
