#!/usr/bin/env python3
# coding=utf-8

from card.firebalt import Firebalt
from hero import Hero


class Jaina(Hero):
    def __init__(self):
        Hero.__init__(self)
        self.name = 'Jaina'
        self.power = Firebalt()
