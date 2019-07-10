#!/usr/bin/env bash
set -exuo pipefail

# Download
curl -L -o raml2http.jar https://github.com/PlatformOfTrust/code-examples-generator/releases/download/latest/raml2http.jar > /dev/null

# Show version
java -jar raml2http.jar --version

# Run
# TODO make it fail in case of 'unknown options' etc.
java -jar raml2http.jar \
     -s ./raml2markdown/src \
     -d $CODE_EXAMPLES \
     -S http \
     -H mockbin.org/request

# Display generated files
find $CODE_EXAMPLES -type f
