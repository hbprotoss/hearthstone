#!/usr/bin/env python3
# coding=utf-8

from card import Power


class ArmorUp(Power):
    def __init__(self):
        Power.__init__(self)
        self.name = '全副武装'

    def post_play(self, engine, target_cards):
        player = engine.cur_player()
        hero = player.hero
        hero.armor = hero.armor + 2
