#!/usr/bin/env python3
# coding=utf-8

from card import Minion


class Test(Minion):
    def __init__(self):
        Minion.__init__(self)
        self.name = '测试'
        self.cost = 1
        self.attack = self.cur_attack = 1
        self.health = self.cur_health = 1
