#!/usr/bin/env bash
set -exuo pipefail


# Download code example generator
curl -L -o raml2http.jar https://github.com/PlatformOfTrust/code-examples-generator/releases/download/latest/raml2http.jar > /dev/null

# Run
java -jar raml2http.jar -s ./raml2markdown/src -d ./code-examples -S http -D mockbin.org/request