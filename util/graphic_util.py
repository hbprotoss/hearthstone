#!/usr/bin/env python3
# coding=utf-8


def print_table(cur_player, opponent_player):
    """
    :param cur_player:
    :param opponent_player:
    :return:
    """

    def print_player_table(player):
        name = player.hero.name
        if player == cur_player:
            name += "(You)"
        print(name.ljust(width))
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
    print_player_table(cur_player)
    print_player_table(opponent_player)


def print_hand_cards(player):
    """
    :param player:
    :return:
    """
    print("-" * 20)
    hand_cards = player.hand_cards
    for index, card in enumerate(hand_cards):
        print("{index}. {minion}".format(index=index, minion=format_card(card)))
    print("-" * 20)


def format_card(card):
    return "{name} [{cost}/{attack}/{health}]".format(name=card.name, cost=card.cur_cost,
                                                      attack=card.cur_attack,
                                                      health=card.cur_health)
