from termpalette.viewers import viewer
from termpalette.util import *
import sys

@viewer('minimal', 'A minimal matrix of colors')
def minimal():

	sys.stdout.write( " " * 4 + " ".join(colornames_short) + "\n" )
	for fg_color, fg_name in enumerate(colornames_short):
		sys.stdout.write(fg_name + " ")
		for bg_color in range(len(colornames_short)):
			sys.stdout.write( color_command( bg(bg_color), fg(fg_color) ) + " ☺ " + color_command() + " ")

		sys.stdout.write("\n")
	sys.stdout.write("\n")
