
'''
Setup for the huygens package

D. C. Groothuizen Dijkema - December, 2019
'''

import setuptools

setuptools.setup(
  author='D. C. Groothuizen Dijkema',
  author_email='',
  name='huygens',
  license='MIT',
  description='huygens is my personal Python library of commonly used functions.',
  version='0.1.0',
  long_description=open('README.md').read(),
  url='https://github.com/DCGroothuizenDijkema/huygens',
  packages=setuptools.find_packages(),
  python_requires='>=3.8.1',
  install_requires=[
  ],
)