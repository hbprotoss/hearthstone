#!/usr/bin/env python3
# coding=utf-8


class Hero(object):
    def __init__(self):
        self.name = ''

        self.attack = 0
        self.heath = 0
        self.armor = 0

        self.immune = False  # 无敌状态

        self.weapon = None  # 武器
        self.power = None  # 英雄技能
