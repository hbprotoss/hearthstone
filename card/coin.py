#!/usr/bin/env python3
# coding=utf-8

from card import Spell


class Coin(Spell):
    def __init__(self):
        Spell.__init__(self)
        self.name = '硬币'

    def post_play(self, engine, target_cards):
        player = engine.cur_player()
        player.cur_mana = player.cur_mana + 1
