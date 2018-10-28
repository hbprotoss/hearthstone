#!/usr/bin/env python3
# coding=utf-8

from card import Card
from player import Player

# 牌桌上玩家分割线
PLAYER_SEPARATE_LINE = '-' * 20
# 牌桌和手牌分割线
TABLE_SEPARATE_LINE = '*' * 20


def print_table(cur_player, opponent_player):
    """
    :param cur_player:
    :param opponent_player:
    :return:
    """

    def print_player_table(player):
        print(format_player(player, player == cur_player))
        print("-" * width)
        for i in range(len(player.table_cards)):
            print("{index}. {minion}".format(index=i, minion=format_card(player.table_cards[i])))

    cur_player_cards = cur_player.table_cards
    opponent_player_cards = opponent_player.table_cards

    blank_width = 10
    width = max(
        max((len(card.name) for card in cur_player_cards), default=0),
        max((len(card.name) for card in opponent_player_cards), default=0),
        len(cur_player.hero.name),
        len(opponent_player.hero.name)
    ) + blank_width
    print('*' * width)
    print_player_table(cur_player)
    print_player_table(opponent_player)
    print('*' * width)


def format_player(player: Player, is_cur_player: bool):
    hero = player.hero
    name = hero.name
    if is_cur_player:
        name += '(你)'
    if hero.armor == 0:
        armor = ''
    else:
        armor = '{armor}🛡️'.format(armor=hero.armor)
    name += ' [{health}💧{sep}{armor} {{{mana}}}]'.format(
        health=hero.health,
        sep='/' if armor else '',
        armor=armor,
        mana=format_mana(player)
    )
    return name


def format_mana(player: Player):
    return '{available_mana}{used_mana} ({available}/{total})'.format(
        available_mana='⬢' * player.cur_mana,
        used_mana='⬡' * (player.mana - player.cur_mana),
        available=player.cur_mana,
        total=player.mana
    )


def print_hand_cards(player: Player):
    """
    :param player:
    :return:
    """
    print(PLAYER_SEPARATE_LINE)
    hand_cards = player.hand_cards
    for index, card in enumerate(hand_cards):
        print("{index}. {minion}".format(index=index, minion=format_card(card)))
    print(PLAYER_SEPARATE_LINE)


def format_card(card: Card):
    return "{name} [{cost}/{attack}/{health}]".format(name=card.name, cost=card.cur_cost,
                                                      attack=card.cur_attack,
                                                      health=card.cur_health)
