#!/usr/bin/env python3
# coding=utf-8

from engine import Engine


def main():
    engine = Engine.get_instance()
    engine.start()


if __name__ == '__main__':
    main()
