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
        _engine = self

    def start(self):
        pass

