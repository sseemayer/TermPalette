# TermPalette

TermPalette is a collection of terminal color palette viewers written in python. They can be accessed using the `tpal` command line utility.

TermPalette is available under the MIT license.

## Installation

### ArchLinux
If you're an ArchLinux user, you can use the [termpalette-git PKGBUILD](https://aur.archlinux.org/packages/termpalette-git/).

### Other *NIX
Clone the repo or download the source, then use the regular python distutils way:

	$ sudo python setup.py install

## Usage

	$ tpal --list
	
	Available viewers:

	name         description
	----         -----------
	art          A colorful art gallery (try doing "art list")
	brightness   A color palette comparing color brightnesses
	matrix       A large matrix showing all color and background combinations for regular and bold text
	minimat      A minimal matrix of colors
	rainbow      A rainbow of colors

	$ tpal minimat

	( a beautiful color preview )

You can also run `tpal` without command line arguments to randomly select a viewer.

## Extending

The available viewers are listed in the `termpalette/viewers/` directory. Viewers make use of the commands in `termpalette.util` to handle drawing colors to the terminal.

