from termpalette.viewers import viewer
from termpalette.util import *
import sys

@viewer('brightness', 'A color palette comparing color brightnesses')
def brightness(args):

	sys.stdout.write("\n")
	sys.stdout.write( " " * 7 + " ".join( " {} ".format(color) for color in colornames_short) + "\n" )

	for bold in range(2):

		sys.stdout.write("bright " if bold else "dark   ")

		for bg_color, bg_name in enumerate(colornames_short):

			if bold:
				sys.stdout.write( color_command( 7, bold, fg(bg_color) ) + " " * 5 + color_command() + " ")
			else: 
				sys.stdout.write( color_command( 7, bold, bg(bg_color) ) + " " * 5 + color_command() + " ")

		sys.stdout.write("\n")
	sys.stdout.write("\n")
