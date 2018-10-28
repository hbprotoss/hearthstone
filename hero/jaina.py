#!/usr/bin/env python3
# coding=utf-8

from card.hero_power.firebalt import Firebalt
from hero import Hero


class Jaina(Hero):
    def __init__(self):
        Hero.__init__(self)
        self.name = '吉安娜'
        self.power = Firebalt()
