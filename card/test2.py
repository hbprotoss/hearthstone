#!/usr/bin/env python3
# coding=utf-8

from card import Minion


class Test2(Minion):
    def __init__(self):
        Minion.__init__(self)
        self.name = 'Test Minion(Type 2)'
        self.cost = self.cur_cost = 1
        self.attack = self.cur_attack = 2
        self.health = self.cur_health = 1
