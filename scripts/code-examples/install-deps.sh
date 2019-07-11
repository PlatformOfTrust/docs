#!/usr/bin/env bash
set -exuo pipefail


# Travis ci Xenial build environment has the following dependencies preinstalled:
# Node.js, Python, JVM and PHP
# https://docs.travis-ci.com/user/reference/xenial

# Node.js
node --version

# Python
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
POETRY_PATH="${HOME}/.poetry/bin"
echo ${POETRY_PATH} >> ${HOME}/.profile
echo ${POETRY_PATH} >> ${HOME}/.bash_profile
export PATH=${PATH}:${POETRY_PATH}
python --version

# Java
java --version

# PHP
phpenv versions
