#!/usr/bin/env python3
# coding=utf-8

_engine = None


class Engine(object):
    @staticmethod
    def get_instance():
        return _engine

    def __init__(self):
        global _engine
        if _engine is not None:
            raise RuntimeError("Engine is initialized")

        self.players = []
        self.player_count = 2
        self.cur_play_idx = 0
        _engine = self

    def start(self):
        pass

    def cur_player(self):
        return self.players[self.cur_play_idx]

    def opponent_player(self):
        return self.players[self.player_count - self.cur_play_idx - 1]
