
import termpalette.viewers
import termpalette.util as u

def list_viewers():
	"""Print a list of registered viewers"""

	print("\nAvailable viewers:\n")
	print(u.color_command(u.underline()) + "name" + u.color_command() + " " * 9 + u.color_command(u.underline()) + "description" + u.color_command())
	for key, viewer in [ (k, termpalette.viewers.registered_viewers[k]) for k in sorted(termpalette.viewers.registered_viewers.keys()) ]:
		print(u.color_command(u.bold(), u.fg(u.colors.BLUE)) + "{:<12}".format(key) + u.color_command() + " {}".format(viewer['desc']))

	print()

def main():

	import optparse, sys, random

	parser = optparse.OptionParser(usage="%prog [options] [viewer_name]")
	parser.add_option('-l', '--list', action='store_true', dest='list', help='List available viewers')

	opt, args = parser.parse_args()

	if opt.list:
		list_viewers()
		sys.exit(0)


	if len(args) == 0:
		selected_viewer = random.choice(list(termpalette.viewers.registered_viewers.keys()))

	else:
		selected_viewer = args[0]


	if not selected_viewer in termpalette.viewers.registered_viewers:
		sys.stderr.write("Unknown viewer: {}\n".format(selected_viewer))
		parser.print_usage();
		sys.exit(1);
		
	termpalette.viewers.registered_viewers[selected_viewer]['func'](args[1:])
