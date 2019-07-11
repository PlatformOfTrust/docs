#!/usr/bin/env bash
set -exuo pipefail


# install the tool
git clone https://github.com/PlatformOfTrust/code-examples-validator
cd code-examples-validator
alias poetry=~/.poetry/bin/poetry
poetry install --no-dev

# run validation
poetry run samples-validator -s ${CODE_EXAMPLES}
cd -

