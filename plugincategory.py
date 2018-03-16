#!/usr/bin/env python
# coding=utf-8

# @file plugin1.py
# @brief plugin1
# @author x565178035,x565178035@126.com
# @version 1.0
# @date 2018-03-16 15:57

from yapsy.IPlugin import IPlugin


class PluginOne(IPlugin):
    def print_name(self):
        pass


class PluginTwo(IPlugin):
    def print_name(self):
        pass


if __name__ == '__main__':
    pass
