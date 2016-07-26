__author__ = 'mark'

import os
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'LICENSE')) as f:
    LICENSE = f.read()
requires = []
dependency_links = []
setup(name='observer',
      version='1.0.6',
      description='A short library which is implements Observer pattern for any classes',
      long_description=README + '\n\n',
      classifiers=[
        "Programming Language :: Python",
        "Library :: Observer",
        ],
      author='Mark Slepkov',
      author_email='self@mark-slepkov.ru',
      url='https://github.com/mark-slepkov/python-observer',
      keywords='observer, event, events',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      dependency_links=dependency_links,
      license=LICENSE
      )
