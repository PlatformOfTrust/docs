#!/usr/bin/env bash
set -exuo pipefail


# Travis ci Xenial build environment has the following dependencies preinstalled:
# Node.js, Python, JVM and PHP
# https://docs.travis-ci.com/user/reference/xenial

# Node.js
node --version

# Python
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
python --version

# Java
java --version

# PHP
phpenv versions
