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
        print("1. Use Hero Power")
        print("2. Attack with Minion")
        print("3. Play Card")
        print("4. Pass Turn")
        action = input("Your choice [1/2/3/4] ")
        return Action(int(action))

    def act_attack_with_minion(self):
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

    def act_use_hero_power(self):
        my_cards, opponent_cards = self.engine.table_cards()
        cur_player = self.engine.cur_player()
        while True:
            target_idx = input("Choose your target: ")
            if not (target_idx.isdigit() or int(target_idx) < 0 or int(target_idx) >= len(opponent_cards)):
                print("Please choose correct minion")
                continue
            target = opponent_cards[int(target_idx)]
            print("You have chosen target %s" % graphic_util.format_card(target))
            break
        cur_player.hero.power.post_play(self.engine, [target])

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
