
'''
Setup for the huygens package

D. C. Groothuizen Dijkema - December, 2019
'''

import setuptools

major=0
minor=2
micro=1

version='{}.{}.{}'.format(major,minor,micro)

setuptools.setup(
  author='D. C. Groothuizen Dijkema',
  author_email='',
  name='huygens',
  license='MIT',
  description='huygens is my personal Python library of commonly used functions.',
  version=version,
  long_description=open('README.md').read(),
  url='https://github.com/DCGroothuizenDijkema/huygens',
  packages=setuptools.find_packages(),
  python_requires='>=3.8.1',
  install_requires=[
    'numpy>=1.18.0',
    'matplotlib>=3.1.2',
    'seaborn>=0.9.0',
  ],
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.8',
  ],
)
