#!/usr/bin/env python3
# coding=utf-8

from card.coin import Coin
from card.test import Test
from card.test2 import Test2
from constant.action import Action
from hero.garrosh import Garrosh
from hero.jaina import Jaina
from player.human import HumanPlayer
from util import graphic_util

_engine = None


class Engine(object):
    @staticmethod
    def get_instance():
        if _engine is None:
            return Engine()
        return _engine

    def __init__(self):
        global _engine
        if _engine is not None:
            raise RuntimeError("Engine is initialized")

        self.players = []
        self.player_count = 2
        self.cur_play_idx = 0
        _engine = self

    def start(self):
        self._init_players()
        while True:
            cur_player = self.cur_player()
            print("%s's turn" % cur_player.hero.name)
            while True:
                print("Table Cards")
                graphic_util.print_table(cur_player, self.opponent_player())
                print("Hand Cards")
                graphic_util.print_hand_cards(cur_player)

                action = cur_player.choose_action()
                print("%s choose %s" % (cur_player.hero.name, action.name))
                self._dispatch_action(action)
                if action == Action.PassTurn:
                    break

                print("Table Cards Now!")
                graphic_util.print_table(cur_player, self.opponent_player())
                print("Hand Cards Now!")
                graphic_util.print_hand_cards(cur_player)

            self.finish_turn()
            print()

    def _dispatch_action(self, action):
        cur_player = self.cur_player()
        if action == Action.AttackWithMinion:
            cur_player.act_attack_with_minion()
            self._clean_dead_minion_on_table(cur_player)
            self._clean_dead_minion_on_table(self.opponent_player())
        elif action == Action.PlayCard:
            cur_player.act_play_card()

    def _clean_dead_minion_on_table(self, player):
        to_remove = []
        for card in player.table_cards:
            if card.cur_health <= 0:
                print("Dead: %s" % graphic_util.format_card(card))
                to_remove.append(card)
        for card in to_remove:
            player.remove_table_card(card)

    def _init_players(self):
        # 先手
        player0 = HumanPlayer(Jaina(), self._generate_jaina_cards())
        player0.hand_cards = [Test()] * 2  # todo for debug
        player0.table_cards = [Test(), Test2()]  # todo for debug
        player0.engine = self
        self.players.append(player0)
        # 后手
        player1 = HumanPlayer(Garrosh(), self._generate_garrosh_cards())
        player1.table_cards = [Test2()]  # todo for debug
        player1.engine = self
        player1.add_hand_card(Coin())
        self.players.append(player1)

    def _generate_jaina_cards(self):
        return [Test()] * 4

    def _generate_garrosh_cards(self):
        return [Test()] * 4

    def cur_player(self):
        return self.players[self.cur_play_idx]

    def opponent_player(self):
        return self.players[self.player_count - self.cur_play_idx - 1]

    def finish_turn(self):
        self.cur_play_idx = self.player_count - self.cur_play_idx - 1

    def table_cards(self):
        """
        :return: [cur player cards list, opponent player cards list]
        """
        return [
            self.cur_player().table_cards,
            self.opponent_player().table_cards
        ]
