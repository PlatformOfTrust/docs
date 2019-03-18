#!/usr/bin/env bash

set -exuo pipefail

# Get and build oas-raml-converter

cd raml2markdown
rm -rf ./oas-raml-converter
git clone https://github.com/mulesoft/oas-raml-converter.git
cd oas-raml-converter
npm install
npm run build

# Fixes running node via shebang on Linux
sed -Ei 's@env node --harmony@env node@' lib/bin/*.js

cd ..

# Install swagger-to-slate node app
npm i -g swagger-to-slate
