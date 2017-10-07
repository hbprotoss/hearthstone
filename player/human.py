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
        graphic_util.print_table(self.engine.cur_player(), self.engine.opponent_player())

    def play_card(self):
        return None

    def add_deck_card(self, card):
        pass
