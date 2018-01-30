#!/urr/bin/env python
# -*- coding:utf-8 -*-

from colpri import ColorPrint


def main():
    c_p = ColorPrint()
    for c_l in c_p.COLORS:
        if c_l is not 'clear':
            print c_p.with_color(c_l, c_l)
    c_p.id_colors()

if __name__ == '__main__':
    main()
