#!/usr/bin/env python3
# coding=utf-8

from card import Power
from engine import Engine


class ArmorUp(Power):
    def __init__(self):
        Power.__init__(self)

    def post_play(self, target_cards):
        engine = Engine.get_instance()
        player = engine.cur_player()
        hero = player.hero
        hero.armor = hero.armor + 2
