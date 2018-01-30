#!/urr/bin/env python
# -*- coding:utf-8 -*-

'''Copyright (c) 2016, Ryo Hanafusa.
All rights reserved.'''

from copy import deepcopy

_COLORS = {
    'clear': '\033[0m',
    'blue': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'cyan': '\033[34m',
    'purple': '\033[35m',
    }


class ColorPrint(object):
    COLORS = deepcopy(_COLORS)

    '''ColorPrint'''
    def __init__(self):
        pass

    def with_color(self, content, colorname):
        if isinstance(content, list):
            output = ' '.join(content)
        else:
            output = content
        return self.COLORS[colorname] + output + self.COLORS['clear']

    def id_colors(self):
        print id(_COLORS)
        print id(self.COLORS)
