from termpalette.viewers import viewer
from termpalette.util import *
import sys, re, functools, random

artworks = {

	# art by pfh - source: http://crunchbang.org/forums/viewtopic.php?pid=157979#p157979
	"ghosts":	"""
			 {1f}   ▄▄▄      {2f}    ▄▄▄      {3f}    ▄▄▄      {4f}    ▄▄▄      {5f}    ▄▄▄      {6f}    ▄▄▄       
			 {1f}  ▀█▀██  ▄  {2f}   ▀█▀██  ▄  {3f}   ▀█▀██  ▄  {4f}   ▀█▀██  ▄  {5f}   ▀█▀██  ▄  {6f}   ▀█▀██  ▄   
			 {1f}▀▄██████▀   {2f} ▀▄██████▀   {3f} ▀▄██████▀   {4f} ▀▄██████▀   {5f} ▀▄██████▀   {6f} ▀▄██████▀    
			 {1f}   ▀█████   {2f}    ▀█████   {3f}    ▀█████   {4f}    ▀█████   {5f}    ▀█████   {6f}    ▀█████    
			 {1f}      ▀▀▀▀▄ {2f}       ▀▀▀▀▄ {3f}       ▀▀▀▀▄ {4f}       ▀▀▀▀▄ {5f}       ▀▀▀▀▄ {6f}       ▀▀▀▀▄  
			""",

	# art by pfh - source: http://crunchbang.org/forums/viewtopic.php?pid=126921#p126921
	"pacman":	"""
			{3f}  ▄███████▄{r}   {1f}  ▄██████▄{r}    {2f}  ▄██████▄{r}    {4f}  ▄██████▄{r}    {5f}  ▄██████▄{r}    {6f}  ▄██████▄{r}
			{3f}▄█████████▀▀{r}  {1f}▄{7f}█▀█{1f}██{7f}█▀█{1f}██▄{r}  {2f}▄{7f}█▀█{2f}██{7f}█▀█{2f}██▄{r}  {4f}▄{7f}█▀█{4f}██{7f}█▀█{4f}██▄{r}  {5f}▄{7f}█▀█{5f}██{7f}█▀█{5f}██▄{r}  {6f}▄{7f}█▀█{6f}██{7f}█▀█{6f}██▄{r}
			{3f}███████▀{r}      {1f}█{7f}▄▄█{1f}██{7f}▄▄█{1f}███{r}  {2f}█{7f}▄▄█{2f}██{7f}▄▄█{2f}███{r}  {4f}█{7f}▄▄█{4f}██{7f}▄▄█{4f}███{r}  {5f}█{7f}▄▄█{5f}██{7f}▄▄█{5f}███{r}  {6f}█{7f}▄▄█{6f}██{7f}▄▄█{6f}███{r}
			{3f}███████▄{r}      {1f}████████████{r}  {2f}████████████{r}  {4f}████████████{r}  {5f}████████████{r}  {6f}████████████{r}
			{3f}▀█████████▄▄{r}  {1f}██▀██▀▀██▀██{r}  {2f}██▀██▀▀██▀██{r}  {4f}██▀██▀▀██▀██{r}  {5f}██▀██▀▀██▀██{r}  {6f}██▀██▀▀██▀██{r}
			{3f}  ▀███████▀{r}   {1f}▀   ▀  ▀   ▀{r}  {2f}▀   ▀  ▀   ▀{r}  {4f}▀   ▀  ▀   ▀{r}  {5f}▀   ▀  ▀   ▀{r}  {6f}▀   ▀  ▀   ▀{r}

			{b}{3f}  ▄███████▄   {1f}  ▄██████▄    {2f}  ▄██████▄    {4f}  ▄██████▄    {5f}  ▄██████▄    {6f}  ▄██████▄{r}
			{b}{3f}▄█████████▀▀  {1f}▄{7f}█▀█{1f}██{7f}█▀█{1f}██▄  {2f}▄{7f}█▀█{2f}██{7f}█▀█{2f}██▄  {4f}▄{7f}█▀█{4f}██{7f}█▀█{4f}██▄  {5f}▄{7f}█▀█{5f}██{7f}█▀█{5f}██▄  {6f}▄{7f}█▀█{6f}██{7f}█▀█{6f}██▄{r}
			{b}{3f}███████▀      {1f}█{7f}▄▄█{1f}██{7f}▄▄█{1f}███  {2f}█{7f}▄▄█{2f}██{7f}▄▄█{2f}███  {4f}█{7f}▄▄█{4f}██{7f}▄▄█{4f}███  {5f}█{7f}▄▄█{5f}██{7f}▄▄█{5f}███  {6f}█{7f}▄▄█{6f}██{7f}▄▄█{6f}███{r}
			{b}{3f}███████▄      {1f}████████████  {2f}████████████  {4f}████████████  {5f}████████████  {6f}████████████{r}
			{b}{3f}▀█████████▄▄  {1f}██▀██▀▀██▀██  {2f}██▀██▀▀██▀██  {4f}██▀██▀▀██▀██  {5f}██▀██▀▀██▀██  {6f}██▀██▀▀██▀██{r}
			{b}{3f}  ▀███████▀   {1f}▀   ▀  ▀   ▀  {2f}▀   ▀  ▀   ▀  {4f}▀   ▀  ▀   ▀  {5f}▀   ▀  ▀   ▀  {6f}▀   ▀  ▀   ▀{r}
			""",

	# art by pfh - source: http://crunchbang.org/forums/viewtopic.php?pid=126921#p126921
	"spaceinvaders": """
			  {b}{1f}▀▄   ▄▀  {r}    {b}{2f}▄▄▄████▄▄▄ {r}   {b}{3f}  ▄██▄  {r}     {b}{4f}▀▄   ▄▀  {r}    {b}{5f}▄▄▄████▄▄▄ {r}   {b}{6f}  ▄██▄  {r}
			 {b}{1f}▄█▀███▀█▄ {r}   {b}{2f}███▀▀██▀▀███{r}   {b}{3f}▄█▀██▀█▄{r}    {b}{4f}▄█▀███▀█▄ {r}   {b}{5f}███▀▀██▀▀███{r}   {b}{6f}▄█▀██▀█▄{r}
			{b}{1f}█▀███████▀█{r}   {b}{2f}▀▀▀██▀▀██▀▀▀{r}   {b}{3f}▀▀█▀▀█▀▀{r}   {b}{4f}█▀███████▀█{r}   {b}{5f}▀▀▀██▀▀██▀▀▀{r}   {b}{6f}▀▀█▀▀█▀▀{r}
			{b}{1f}▀ ▀▄▄ ▄▄▀ ▀{r}   {b}{2f}▄▄▀▀ ▀▀ ▀▀▄▄{r}   {b}{3f}▄▀▄▀▀▄▀▄{r}   {b}{4f}▀ ▀▄▄ ▄▄▀ ▀{r}   {b}{5f}▄▄▀▀ ▀▀ ▀▀▄▄{r}   {b}{6f}▄▀▄▀▀▄▀▄{r}
			
			  {1f}▀▄   ▄▀  {r}    {2f}▄▄▄████▄▄▄ {r}   {3f}  ▄██▄  {r}     {4f}▀▄   ▄▀  {r}    {5f}▄▄▄████▄▄▄ {r}   {6f}  ▄██▄  {r}
			 {1f}▄█▀███▀█▄ {r}   {2f}███▀▀██▀▀███{r}   {3f}▄█▀██▀█▄{r}    {4f}▄█▀███▀█▄ {r}   {5f}███▀▀██▀▀███{r}   {6f}▄█▀██▀█▄{r}
			{1f}█▀███████▀█{r}   {2f}▀▀▀██▀▀██▀▀▀{r}   {3f}▀▀█▀▀█▀▀{r}   {4f}█▀███████▀█{r}   {5f}▀▀▀██▀▀██▀▀▀{r}   {6f}▀▀█▀▀█▀▀{r}
			{1f}▀ ▀▄▄ ▄▄▀ ▀{r}   {2f}▄▄▀▀ ▀▀ ▀▀▄▄{r}   {3f}▄▀▄▀▀▄▀▄{r}   {4f}▀ ▀▄▄ ▄▄▀ ▀{r}   {5f}▄▄▀▀ ▀▀ ▀▀▄▄{r}   {6f}▄▀▄▀▀▄▀▄{r}
			

			                                     {7f}▌{r}
			
			                                   {7f}▌{r}
			                                   {7f}{r}
			                                  {7f}▄█▄{r}
			                              {7f}▄█████████▄{r}
			                              {7f}▀▀▀▀▀▀▀▀▀▀▀{r}
			""",

	# art by pfh - source: http://crunchbang.org/forums/viewtopic.php?pid=127737#p127737
	"yinyang":	"""
			{1f}▒▒▒▒{r} {b}{1f}▒▒{r}   {2f}▒▒▒▒{r} {b}{2f}▒▒{r}   {3f}▒▒▒▒{r} {b}{3f}▒▒{r}   {4f}▒▒▒▒{r} {b}{4f}▒▒{r}   {5f}▒▒▒▒{r} {b}{5f}▒▒{r}   {6f}▒▒▒▒{r} {b}{6f}▒▒{r} 
			{1f}▒▒ ■{r} {b}{1f}▒▒{r}   {2f}▒▒ ■{r} {b}{2f}▒▒{r}   {3f}▒▒ ■{r} {b}{3f}▒▒{r}   {4f}▒▒ ■{r} {b}{4f}▒▒{r}   {5f}▒▒ ■{r} {b}{5f}▒▒{r}   {6f}▒▒ ■{r} {b}{6f}▒▒{r}  
			{1f}▒▒ {r}{b}{1f}▒▒▒▒{r}   {2f}▒▒ {r}{b}{2f}▒▒▒▒{r}   {3f}▒▒ {r}{b}{3f}▒▒▒▒{r}   {4f}▒▒ {r}{b}{4f}▒▒▒▒{r}   {5f}▒▒ {r}{b}{5f}▒▒▒▒{r}   {6f}▒▒ {r}{b}{6f}▒▒▒▒{r}  
			""",
	

	# art by ivo - source: http://crunchbang.org/forums/viewtopic.php?pid=134749#p134749
	"abcdef":	"""
			{b}{1f}   ██████  {r} {b}{2f}██████   {r}{b}{3f}  ██████{r} {b}{4f}██████  {r} {b}{5f}  ██████{r} {b}{6f}  ███████{r}
			{b}{1f}   ████████{r} {b}{2f}██    ██ {r}{b}{3f}██      {r} {b}{4f}██    ██{r} {b}{5f}██████  {r} {b}{6f}█████████{r}
			{1f}   ██  ████{r} {2f}██  ████ {r}{3f}████    {r} {4f}████  ██{r} {5f}████    {r} {6f}█████    {r}
			{1f}   ██    ██{r} {2f}██████   {r}{3f}████████{r} {4f}██████  {r} {5f}████████{r} {6f}██       {r} 
			""",
	
	# art by pfh - source: http://crunchbang.org/forums/viewtopic.php?pid=139126#p139126
	"dashes":	"""
			{1f}▬▬▬▬▬ {2f}▬▬▬▬▬ {3f}▬▬▬▬▬ {4f}▬▬▬▬▬ {5f}▬▬▬▬▬ {6f}▬▬▬▬▬
			{b}{1f}▬▬▬▬▬ {2f}▬▬▬▬▬ {3f}▬▬▬▬▬ {4f}▬▬▬▬▬ {5f}▬▬▬▬▬ {6f}▬▬▬▬▬
			""",


}

@viewer('art', 'A colorful art gallery (try doing "art list")')
def art(argv):
	
	if "list" in argv or "l" in argv:
		print("\n" + color_command(underline()) + "Available artworks:" + color_command())
		print("\n".join(sorted(artworks.keys())))
		print()
		sys.exit(0)

	artwork = argv[0] if len(argv) > 0 else random.choice(list(artworks.keys()))


	if artwork not in artworks:
		print("Unknown artwork '{}'. Try doing 'art list' to see which ones are available.\n".format(artwork))
		sys.exit(3)

	sub_steps = [
		(r'^\t+', r''),		
		(r'{r}', color_command()),
		(r'{b}', color_command(bold())),
		(r'{i}', color_command(italic())),
		(r'{u}', color_command(underline())),
		
	]

	sub_steps.extend( ( r"\{{{}f\}}".format(i), color_command(fg(i)) ) for i in range(9) )
	sub_steps.extend( ( r"\{{{}b\}}".format(i), color_command(bg(i)) ) for i in range(9) )


	aw = artworks[artwork].split('\n')

	aw = functools.reduce(lambda x, f: [re.sub(f[0], f[1], l) for l in x], sub_steps, aw)


	print("\n".join(aw)) 
