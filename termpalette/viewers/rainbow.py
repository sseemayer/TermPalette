from termpalette.viewers import viewer
from termpalette.util import *
import sys

@viewer('rainbow', 'A rainbow of colors')
def rainbow(args):
	"""Draw a pretty ANSI rainbow
	original idea by crshd - source: http://crunchbang.org/forums/viewtopic.php?pid=128584#p128584
	"""

	sys.stdout.write("\n")

	for bold in range(2):

		sys.stdout.write("  brt " if bold else "  drk ")

		for f in range(7):
			sys.stdout.write(color_command(bold, bg(f+1), fg(f)) + "██▓▒░")
		
		sys.stdout.write(color_command(fg(7)) + "██" + color_command())

		sys.stdout.write("\n\n")

