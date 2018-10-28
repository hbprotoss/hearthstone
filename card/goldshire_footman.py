#!/usr/bin/env python3
# coding=utf-8

from card import Minion


class GoldshireFootman(Minion):
    def __init__(self):
        Minion.__init__(self)
        self.name = '闪金镇步兵'
        self.cost = self.cur_cost = 1
        self.attack = self.cur_attack = 1
        self.health = self.cur_health = 2
