#!/usr/bin/env bash
set -exuo pipefail

# Download
curl -L -o raml2http.jar https://github.com/PlatformOfTrust/code-examples-generator/releases/download/latest/raml2http.jar > /dev/null

# Show version
java -jar raml2http.jar --version

# Run code examples generator
# TODO make it fail in case of 'unknown options' etc.
java -jar raml2http.jar \
     -s ./raml2markdown/src \
     -d $CODE_EXAMPLES \
     -S $SCHEME \
     -H $HOST
