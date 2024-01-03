# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from setuptools import setup, find_packages

setup(
    name='lastfm-api',
    version='1.0.0',
    packages=find_packages(exclude=['.venv']),
    url='https://github.com/pkeorley/lastfm-api',
    license='MIT',
    licence_files=['LICENSE'],
    author='pkeorley',
    author_email='pkeorley@gmail.com',
    description='A tool that helps to work effectively with the API from last.fm'
)