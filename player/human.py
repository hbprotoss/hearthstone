#!/usr/bin/env python3
# coding=utf-8

from constant.action import Action
from player import Player
from util import graphic_util


def print_cards(on_begin=True, on_end=True):
    def decorator(func):
        def wrapper(self):
            if on_begin:
                print("Table Cards")
                graphic_util.print_table(self, self.engine.opponent_player())
                print("Hand Cards")
                graphic_util.print_hand_cards(self)

            ret = func(self)

            if on_end:
                print("Table Cards Now!")
                graphic_util.print_table(self, self.engine.opponent_player())
                print("Hand Cards Now!")
                graphic_util.print_hand_cards(self)

            return ret

        return wrapper

    return decorator


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

    @print_cards(on_end=False)
    def act_attack(self):
        my_cards, opponent_cards = self.engine.table_cards()
        while True:
            minion_idx = input("Choose your minion to attack: ")
            if not (minion_idx.isdigit() or int(minion_idx) < 0 or int(minion_idx) >= len(my_cards)):
                print("Please choose correct minion")
                continue
            minion = my_cards[int(minion_idx)]
            print("You have chosen minion %s" % graphic_util.format_card(minion))
            break

        while True:
            target_idx = input("Choose your target: ")
            if not (target_idx.isdigit() or int(target_idx) < 0 or int(target_idx) >= len(opponent_cards)):
                print("Please choose correct minion")
                continue
            target = opponent_cards[int(target_idx)]
            print("You have chosen target %s" % graphic_util.format_card(target))
            break

        minion.cur_health -= target.cur_attack
        target.cur_health -= minion.cur_attack

    @print_cards()
    def act_play_card(self):
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

    def play_card(self):
        return None

    def add_deck_card(self, card):
        pass

