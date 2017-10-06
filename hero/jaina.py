#!/usr/bin/env python3
# coding=utf-8

from hero import Hero
from card.firebalt import Firebalt


class Jaina(Hero):
    def __init__(self):
        Hero.__init__(self)
        self.power = Firebalt()