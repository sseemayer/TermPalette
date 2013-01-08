from termpalette.viewers import viewer
from termpalette.util import *
import sys

@viewer('minimat', 'A minimal matrix of colors')
def minimat(args, labels=colornames_short):

	cell = " ☻ " if len(args) == 0 else args[0]

	labellen = max( len(cn) for cn in labels )
	cellsize = max( labellen, len(cell) )

	sys.stdout.write( "\n   " + " " * (labellen+1) + " ".join( "{:^{}}".format( cn, cellsize) for cn in labels ) + "\n" )
	for fg_color, fg_name in enumerate(labels):
		sys.stdout.write("   {:>{}} ".format(fg_name, labellen))
		for bg_color in range(len(labels)):
			sys.stdout.write( color_command( bg(bg_color), fg(fg_color) ) + "{:^{}}".format(cell, cellsize) + color_command() + " ")

		sys.stdout.write("\n")
	sys.stdout.write("\n")
