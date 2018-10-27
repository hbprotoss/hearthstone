#!/usr/bin/env python3
# coding=utf-8


class Hero(object):
    def __init__(self):
        self.name = ''

        self.attack = 0
        self.heath = 0
        self.armor = 0

        self.weapon = None  # 武器
        self.power = None  # 英雄技能

        self.is_immune = False  # 无敌状态
        self.is_weapon_attacked = False  # 是否使用过武器
        self.is_power_attacked = False  # 是否使用过英雄技能
