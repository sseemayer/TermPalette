import itertools

def enum(*sequential, **named):
	enums = dict(zip(sequential, range(len(sequential))), **named)
	return type('Enum', (), enums)

def color_command(*argv):
	return "\33[" + ";".join( str(a) for a in argv ) + "m"

def fg(*argv):
	if len(argv) == 1:
		return 30 + argv[0]
	else:
		return [30 + a for a in argv]

def bg(*argv):
	if len(argv) == 1:
		return 40 + argv[0]
	else:
		return [40 + a for a in argv]

def bold():
	return 1

def italic():
	return 3

def underline():
	return 4


colors = enum('BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE', 'DEFAULT')

colornames_long  = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'default']
colornames_short = ['blk', 'red', 'grn', 'yel', 'blu', 'mag', 'cya', 'wht', 'def']
