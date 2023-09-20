from setuptools import setup, find_packages
import os


def read(filename):
	return open(os.path.join(os.path.dirname(__file__), filename)).read()


# python3 setup.py install
setup(
	name="uniaddon",
	version="0.0.1.070923",
	author="stpatriarch",
	author_email="chinaryannarek@gmail.com",
	description="United additional funitions for any commerical software.",
	license="GNU General Public License v3.0",
	keywords="",
	url="",
	packages=find_packages(),
	long_description=read('README.md'),
	classifiers=[
		"Development Status :: 1 - Alpha",
		"Topic :: Utilities",
		"License :: GNU General Public License v3.0",
	],
)