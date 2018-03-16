#!/usr/bin/env python
# coding=utf-8

# @file yapsy-example.py
# @brief yapsy-example
# @author x565178035,x565178035@126.com
# @version 1.0
# @date 2018-03-16 15:17


from yapsy.PluginManager import PluginManager

import plugincategory as category


def main():
    # Load the plugins from the plugin directory.
    manager = PluginManager()
    manager.setPluginPlaces(["plugins\\plugins1", "plugins\\plugins2"])

    manager.setCategoriesFilter({
        "PluginOne": category.PluginOne,
        "PluginTwo": category.PluginTwo,
    })

    print { "PluginOne": category.PluginOne, "PluginTwo": category.PluginTwo }
    manager.collectPlugins()
    print manager.getPluginsOfCategory("PluginTwo")
    for plugin in manager.getPluginsOfCategory("PluginTwo"):
        plugin.plugin_object.print_name()


    # for plugin in manager.getAllPlugins():
    #     plugin.plugin_object.print_name()


if __name__ == "__main__":
    main()
