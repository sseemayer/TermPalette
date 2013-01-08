import pkgutil
import sys
import os

registered_viewers = {}

def viewer(key, desc):

	def _decorator(f):
		registered_viewers[key] = {
			'func': f,
			'desc': desc
		}
		return f

	return _decorator


dirname = os.path.dirname( os.path.realpath(__file__) )

for importer, package_name, _ in pkgutil.iter_modules([dirname]):
	full_package_name = '%s.%s' % (dirname, package_name)
	importer.find_module(package_name).load_module(package_name)
