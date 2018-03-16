#!/usr/bin/env python
# coding=utf-8

# @file plugin1.py
# @brief plugin1
# @author x565178035,x565178035@126.com
# @version 1.0
# @date 2018-03-16 15:19

import plugincategory


class PluginOne(plugincategory.PluginOne):
    def print_name(self):
        print "This is plugin 1"
