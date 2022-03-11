#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

"""Archivo de configuracion del paquete transfer.

Se crea la ruta del archivo de configuracion en caso de no existir
Linux: $HOME/.config/transfer
Windows: C://$APPDATA/transfer

Se registra el comando rsp-transfer2elk en la variable PATH
"""

from setuptools import setup, find_packages
import os
import sys

setuppath = os.path.dirname(os.path.abspath(__file__))

# retrieve the version
try:
    versionfile = os.path.join(setuppath, 'transfer', '__version__.py')
    f = open(versionfile, 'r')
    content = f.readline()
    splitcontent = content.split('\'')
    version = splitcontent[1]
    f.close()
except:
    raise Exception(
        'Could not determine the version from transfer/__version__.py')

if sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
    _config_dir = '{}/transfer'.format(os.environ['APPDATA'])
else:
    _config_dir = '{}/.config/transfer'.format(os.getenv('HOME'))

data_files = []
if not os.path.exists(os.path.join(_config_dir, 'config.yml')):
    os.makedirs(_config_dir, exist_ok=True)
    data_files.append((_config_dir, ['cfg/config.yml']))

# run the setup command
setup(
    name='transfer',
    version=version,
    license='RichIT license',
    description='Interta los archivos .txt en el indice transfer y guarda una \
        copia en formato csv de esos archivos',
    long_description=open(os.path.join(setuppath, 'README.rst')).read(),
    url='',
    author='acruz@richit.ai',
    author_email='acruz@richit.ai',
    packages=find_packages(),
    install_requires=['elasticsearch', 'pyyaml', 'redis'],
    classifiers=['Programming Language :: Python :: 3'],
    entry_points={'console_scripts': [
        'transfer2elk=transfer.commands.transfer:transfer2elk',
        'transferSource=transfer.commands.transfer:transferSource',
    ]},
    data_files=data_files,
)
