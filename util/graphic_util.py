#!/usr/bin/env python3
# coding=utf-8


def print_table(cur_player, opponent_player):
    """
    :param cur_player:
    :param opponent_player:
    :return:
    """
    cur_player_cards = cur_player.table_cards
    opponent_player_cards = opponent_player.table_cards

    blank_width = 10
    height = max(len(cur_player_cards), len(opponent_player_cards))
    width = max(
        max((len(card.name) for card in cur_player_cards), default=0),
        max((len(card.name) for card in opponent_player_cards), default=0),
        len(cur_player.hero.name),
        len(opponent_player.hero.name)
    ) + blank_width
    print("%s|%s" % (cur_player.hero.name.ljust(width), opponent_player.hero.name.ljust(width)))
    print("-" * (width * 2 + 1))


def print_hand_cards(player):
    """
    :param player:
    :return:
    """
    print("-" * 20)
    hand_cards = player.hand_cards
    for index, card in enumerate(hand_cards):
        print("{index}. {name} [{cost}/{attack}/{health}]".format(name=card.name, cost=card.cur_cost,
                                                                  attack=card.cur_attack,
                                                                  health=card.cur_health, index=index)
              )
    print("-" * 20)
