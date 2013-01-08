from termpalette.viewers import viewer
from termpalette.util import *
import sys

@viewer('minimal', 'A minimal matrix of colors')
def minimal(cell=" ☻ ", labels=colornames_short):

	labellen = max( len(cn) for cn in labels )
	cellsize = max( labellen, len(cell) )

	sys.stdout.write( " " * (labellen+1) + " ".join( "{:^{}}".format( cn, cellsize) for cn in labels ) + "\n" )
	for fg_color, fg_name in enumerate(labels):
		sys.stdout.write("{:>{}} ".format(fg_name, labellen))
		for bg_color in range(len(labels)):
			sys.stdout.write( color_command( bg(bg_color), fg(fg_color) ) + "{:^{}}".format(cell, cellsize) + color_command() + " ")

		sys.stdout.write("\n")
	sys.stdout.write("\n")
