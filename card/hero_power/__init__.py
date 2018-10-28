#!/usr/bin/env python3
# coding=utf-8

from card import Spell


class Power(Spell):
    def __init__(self):
        Spell.__init__(self)
        self.power = True

    def has_target(self):
        return True
