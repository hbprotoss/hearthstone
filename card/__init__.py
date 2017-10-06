#!/usr/bin/env python3
# coding=utf-8

from constant.race import Race


class Card(object):
    def __init__(self):
        self.attack = 0  # 初始攻击力
        self.cur_attack = 0  # 当前攻击力
        self.health = 0  # 初始生命值
        self.cur_health = 0  # 当前生命值
        self.cost = 0  # 初始费用
        self.cur_cost = 0  # 当前费用

        self.minion = False  # 随从
        self.spell = False  # 法术
        self.weapon = False  # 武器
        self.power = False  # 英雄技能

        self.effect = False  # 卡牌效果
        self.battleCry = False  # 战吼
        self.charge = False  # 冲锋
        self.stealth = False  # 潜行
        self.combo = False  # 连击
        self.deathRattle = False  # 亡语
        self.divineShield = False  # 圣盾
        self.overload = False  # 过载
        self.secret = False  # 奥秘
        self.taunt = False  # 嘲讽
        self.windFury = False  # 风怒
        self.enrage = False  # 激怒
        self.spellDamage = False  # 法伤
        self.chooseOne = False  # 抉择
        self.poisonous = False  # 剧毒

    def pre_turn(self):
        """
        回合开始前处理
        效果
        :return:
        """
        pass

    def post_turn(self):
        """
        回合结束后处理
        效果
        :return:
        """
        pass

    def pre_play(self):
        """
        出牌前处理
        战吼
        :return:
        """
        pass

    def post_play(self):
        """
        出牌后处理
        战吼，冲锋，连击，圣盾，过载，奥秘，沉默，潜行，嘲讽，风怒，抉择
        各种法术效果
        :return:
        """
        pass

    def pre_dead(self):
        """
        死亡前处理
        可能有各种特效，一时忘了
        :return:
        """
        pass

    def post_dead(self):
        """
        死亡后处理
        亡语
        :return:
        """
        pass


class Minion(Card):
    def __init__(self):
        Card.__init__(self)
        self.minion = True
        self.minion_race = Race.Normal


class Spell(Card):
    def __init__(self):
        Card.__init__(self)
        self.spell = True


class Weapon(Card):
    def __init__(self):
        Card.__init__(self)
        self.weapon = True


class Power(Card):
    def __init__(self):
        Card.__init__(self)
        self.power = True
