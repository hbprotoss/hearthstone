#!/usr/bin/env python3
# coding=utf-8

from card import Power


class Firebalt(Power):
    def __init__(self):
        Power.__init__(self)
        self.name = 'Firebalt'
        self.attack = self.cur_attack = 1
        self.target_count = 1

    def post_play(self, engine, target_cards):
        assert len(target_cards) == 1
        target = target_cards[0]
        target.cur_health = target.cur_health - self.cur_attack
