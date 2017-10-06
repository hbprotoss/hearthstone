#!/usr/bin/env python3
# coding=utf-8


class Player(object):
    def __init__(self, hero):
        self.hero = hero
        self.mana = 0
        self.cur_mana = 0
        self.locked_mana = 0

        self.hand_cards = []  # 手牌
        self.deck_cards = []  # 牌库
        self.dead_cards = []  # 坟场

    def draw_card_from_deck(self, from_top=True):
        """
        抓牌
        :return: Card
        """
        card = self.remove_deck_card(from_top)
        self.add_hand_card(card)

    def add_hand_card(self, card):
        """
        增加手牌
        :param card:
        :return:
        """

    def remove_hand_card(self, card):
        """
        移除手牌
        :param card:
        :return: Card
        """

    def add_deck_card(self, card):
        """
        由场上效果增加牌库
        :param card:
        :return:
        """

    def remove_deck_card(self, from_top=True):
        """
        移除牌库中的牌
        :param from_top:
        :return: Card
        """
        return None

    def play_card(self):
        """
        出牌
        :return: Card
        """
