#!/usr/bin/env bash
set -exuo pipefail

# make poetry available
export PATH=${PATH}:${HOME}/.poetry/bin

# install the tool
git clone https://github.com/PlatformOfTrust/code-examples-validator
cd code-examples-validator
poetry install --no-dev

# run validation
poetry run samples-validator -s "../${CODE_EXAMPLES}"
cd -

