#!/usr/bin/env bash
set -exuo pipefail

# make poetry available
export PATH=${PATH}:${HOME}/.poetry/bin

# install the tool
git clone https://github.com/PlatformOfTrust/code-examples-validator
cd code-examples-validator
poetry install --no-dev

# Display validator conf
cat ../scripts/code-examples/validator_conf.yml

# run validation
# Use custom configuration file to be able to ignore unstable API resources
poetry run samples-validator -s $CODE_EXAMPLES -c $VALIDATOR_CONF
cd -
