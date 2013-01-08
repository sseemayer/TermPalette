from distutils.core import setup

setup(	name='TermPalette',
	version='0.1',
	author='Stefan Seemayer',
	author_email='mail@semicolonsoftware.de',
	url='https://github.com/sseemayer/TermPalette',

	packages=['termpalette', 'termpalette.viewers'],
	scripts=['tpal']
)
