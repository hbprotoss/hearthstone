#!/usr/bin/env python3
# coding=utf-8

from card.coin import Coin
from card.test import Test
from hero.garrosh import Garrosh
from hero.jaina import Jaina
from player.human import HumanPlayer

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
            cur_player = self.players[self.cur_play_idx]
            print("%s's turn" % cur_player.hero.name)
            action = cur_player.choose_action()
            print("%s choose %s" % (cur_player.hero.name, action.name))

            self.finish_turn()
            print()

    def _init_players(self):
        # 先手
        player0 = HumanPlayer(Jaina(), self._generate_jaina_cards())
        self.players.append(player0)
        # 后手
        player1 = HumanPlayer(Garrosh(), self._generate_garrosh_cards())
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
