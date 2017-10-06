#!/usr/bin/env python3
# coding=utf-8

from hero import Hero
from card.armor_up import ArmorUp


class Garrosh(Hero):
    def __init__(self):
        Hero.__init__(self)
        self.power = ArmorUp()