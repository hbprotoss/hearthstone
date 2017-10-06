#!/usr/bin/env python3
# coding=utf-8

from card.coin import Coin
from card.test import Test
from hero.garrosh import Garrosh
from hero.jaina import Jaina
from player import Player

_engine = None


class Engine(object):
    @staticmethod
    def get_instance():
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

    def _init_players(self):
        # 先手
        player0 = Player(Jaina(), self._generate_jaina_cards())
        self.players.append(player0)
        # 后手
        player1 = Player(Garrosh(), self._generate_garrosh_cards())
        player1.add_hand_card(Coin())
        self.players.append(player1)

    def _generate_jaina_cards(self):
        return [Test()]

    def _generate_garrosh_cards(self):
        return [Test()]

    def cur_player(self):
        return self.players[self.cur_play_idx]

    def opponent_player(self):
        return self.players[self.player_count - self.cur_play_idx - 1]
