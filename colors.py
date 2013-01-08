#!/usr/bin/env python

# see http://pueblo.sourceforge.net/doc/manual/ansi_color_codes.html for ANSI codes

import sys

colors_long  = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'default']
colors_short = ['blk', 'red', 'grn', 'yel', 'blu', 'mag', 'cya', 'wht', 'def']

def colors_tabular():

    for i in range(2):

        sys.stdout.write( " " * 8 + " ".join( "{:^7}".format(color) for color in colors_long) + "\n" )

        for j in range(30, 39):
            sys.stdout.write("{:>7} ".format(colors_long[j-30]))
            for k in range(40, 49):
                    sys.stdout.write("\33[%d;%d;%dm%d;%d;%d\33[m " % (i, j, k, i, j, k),)

            sys.stdout.write("\n")
        sys.stdout.write("\n")





# vim: set et sw=4 ts=4:
