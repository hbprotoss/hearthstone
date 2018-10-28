#!/usr/bin/env python3
# coding=utf-8

from constant.action import Action
from player import Player
from util import graphic_util


class HumanPlayer(Player):
    def __init__(self, hero, deck_cards):
        Player.__init__(self, hero, deck_cards)

    def choose_action(self):
        # print("Choose Action:")
        # print("1. Use Hero Power")
        # print("2. Attack with Minion")
        # print("3. Play Card")
        # print("4. Pass Turn")
        print('选择操作')
        print('1. 使用英雄技能')
        print('2. 用随从攻击')
        print('3. 出牌')
        print('4. 结束回合')
        action = input("你的选择 [1/2/3/4] ")
        return Action(int(action))

    def act_attack_with_minion(self):
        my_cards, opponent_cards = self.engine.table_cards()
        while True:
            minion_idx = input("选择你的随从: ")
            if not (minion_idx.isdigit() or int(minion_idx) < 0 or int(minion_idx) >= len(my_cards)):
                print("请选择正确随从")
                continue
            minion = my_cards[int(minion_idx)]
            print("你选择了%s" % graphic_util.format_card(minion))
            break

        while True:
            target_idx = input("选择你的攻击目标: ")
            if not (target_idx.isdigit() or int(target_idx) < 0 or int(target_idx) >= len(opponent_cards)):
                print("请选择正确目标")
                continue
            target = opponent_cards[int(target_idx)]
            print("你选择了目标%s" % graphic_util.format_card(target))
            break

        minion.cur_health -= target.cur_attack
        target.cur_health -= minion.cur_attack

    def act_use_hero_power(self):
        my_cards, opponent_cards = self.engine.table_cards()
        cur_player = self.engine.cur_player()
        targets = []
        if cur_player.hero.power.has_target():
            while True:
                target_idx = input("请选择攻击目标: ")
                if not (target_idx.isdigit() or int(target_idx) < 0 or int(target_idx) >= len(opponent_cards)):
                    print("请选择正确目标")
                    continue
                target = opponent_cards[int(target_idx)]
                print("你选择了目标%s" % graphic_util.format_card(target))
                targets.append(target)
                break
        cur_player.hero.power.post_play(self.engine, targets)

    def act_play_card(self):
        while True:
            card_idx = input("请选择要出的牌: ")
            if not (card_idx.isdigit() or int(card_idx) < 0 or int(card_idx) >= len(self.hand_cards)):
                print("请选择正确的牌")
                continue
            card_to_play = self.hand_cards[int(card_idx)]
            if self.cur_mana < card_to_play.cur_cost:
                print('法力水晶不足')
                return
            self.remove_hand_card(card_to_play)
            self.cur_mana -= card_to_play.cur_cost
            break

        while True:
            place_idx = input("请选择放置位置")
            if not (place_idx.isdigit() or int(place_idx) < -1 or int(place_idx) > len(self.table_cards)):
                print("请选择正确位置")
                continue
            self.add_table_card(card_to_play, int(place_idx))
            break

    def add_deck_card(self, card):
        pass
