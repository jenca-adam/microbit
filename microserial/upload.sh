#!/bin/bash
rm -r dist
python setup.py sdist >/dev/null
list=dist/*
twine upload $list
