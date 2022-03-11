#!/usr/bin/env bash

python setup.py sdist
pip install --user dist/transfer-2.3.0.tar.gz
