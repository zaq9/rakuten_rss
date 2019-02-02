from codecs import open

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setup(
	name='rakuten_rss',
	version='0.0.1',
	description='Python module for Rakuten RSS',
	long_description=long_description,
	url='https://github.com/zaq9/rakuten_rss',
	author='zaq',
	author_email='zaq_9@yahoo.co.jp',

	classifiers=[
		# How mature is this project? Common values are
		#   3 - Alpha
		#   4 - Beta
		#   5 - Production/Stable
		'Development Status :: 3 - Alpha',
		'Programming Language :: Python :: 3',
	],
	keywords=['python', 'finance', 'MarketData', 'RakutenRSS'],
	# py_modules=['nk225op'],
	license='MIT',
	packages=find_packages(exclude=('docs')),
	install_requires=[],
)
