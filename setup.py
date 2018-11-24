#!/usr/bin/env python

from setuptools import setup

setup(name='meson-check',
      version='0.1.0',
      description='Check module for Meson build system',
      license='Apache v2',
      author='Snaipe',
      author_email='me@snai.pe',
      url='https://snai.pe/git/meson-check',
      packages=['mesonbuild.modules'],
      install_requires=['meson', 'lark']
     )
