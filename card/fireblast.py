#!/usr/bin/env python3
# coding=utf-8

from card import Power


class Fireblast(Power):
    def __init__(self):
        Power.__init__(self)
        self.attack = self.cur_attack = 1
        self.cost = self.cur_cost = 2
