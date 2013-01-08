# TermPalette

TermPalette is a collection of terminal color palette viewers written in python. They can be accessed using the `tpal` command line utility.

TermPalette is available under the MIT license.

## Usage

	$ tpal --list
	
	Available viewers:

	name         description
	----         -----------
	matrix       A large matrix of colors
	minimal      A minimal matrix of colors

	$ tpal minimal

	( a beautiful color preview )

You can also run `tpal` without command line arguments to randomly select a viewer.

## Extending

The available viewers are listed in the `termpalette/viewers/` directory. Viewers make use of the commands in `termpalette.util` to handle drawing colors to the terminal.

