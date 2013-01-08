from termpalette.viewers import viewer
from termpalette.util import *
import sys

@viewer('matrix', 'A large matrix of colors')
def matrix():

	for bold in range(2):

		sys.stdout.write( " " * 8 + " ".join( "{:^7}".format(color) for color in colornames_long) + "\n" )
		for fg_color, fg_name in enumerate(colornames_long):
			sys.stdout.write("{:>7} ".format(fg_name))
			for bg_color in range(len(colornames_long)):
				sys.stdout.write( color_command( bold, bg(bg_color), fg(fg_color) ) + "{};{};{}".format(bold, bg(bg_color), fg(fg_color)) + color_command() + " ")

			sys.stdout.write("\n")
		sys.stdout.write("\n")