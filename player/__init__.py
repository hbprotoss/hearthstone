#!/usr/bin/env python3
# coding=utf-8


class Player(object):
    def __init__(self, hero, deck_cards):
        self.hero = hero
        self.mana = 1
        self.cur_mana = 1
        self.locked_mana = 0

        self.hand_cards = []  # 手牌
        self.deck_cards = deck_cards  # 牌库
        self.table_cards = []  # 桌面上的牌
        self.dead_cards = []  # 坟场

        self.engine = None

    def choose_action(self):
        raise NotImplementedError

    def act_attack_with_minion(self):
        raise NotImplementedError

    def act_use_hero_power(self):
        raise NotImplementedError

    def act_play_card(self):
        raise NotImplementedError

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
        self.hand_cards.append(card)

    def remove_hand_card(self, card):
        """
        移除手牌
        :param card:
        :return: Card
        """
        self.hand_cards.remove(card)

    def add_deck_card(self, card):
        """
        由场上效果增加牌库
        :param card:
        :return:
        """
        raise NotImplementedError

    def remove_deck_card(self, from_top=True):
        """
        移除牌库中的牌
        :param from_top:
        :return: Card
        """
        if len(self.deck_cards) == 0:
            return None
        return self.deck_cards.pop(0)

    def add_table_card(self, card, index):
        """
        增加桌面上的牌
        :param card:
        :param index:
        :return:
        """
        if index == -1 or index == len(self.table_cards):
            self.table_cards.append(card)
        else:
            self.table_cards.insert(index, card)

    def remove_table_card(self, card):
        self.table_cards.remove(card)

    def play_card(self):
        """
        出牌
        :return: Card
        """
        raise NotImplementedError
