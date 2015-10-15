import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


version = '0.0.0'

install_requires = [
]

if sys.version_info >= (3,):
    install_requires.append('scapy-python3>=2.3.1')
else:
    install_requires.append('scapy>=2.3.1')


setup(
    name='pybench',
    version=version,
    description='SDN benchmarking tool',
    long_description=README,
    author='Kjwon15',
    author_email='kjwonmail@gmail.com',
    url='https://github.com/Kjwon15/pybench',
    packages=find_packages(),
    py_modules=['pybench'],
    zip_safe=False,
    install_requires=install_requires,
)
