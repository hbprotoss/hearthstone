#!/usr/bin/env python3
# coding=utf-8

from card.armor_up import ArmorUp
from hero import Hero


class Garrosh(Hero):
    def __init__(self):
        Hero.__init__(self)
        self.power = ArmorUp()
