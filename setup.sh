#!/usr/bin/env bash

set -exuo pipefail

# Get and build oas-raml-converter

cd raml2markdown
rm -rf ./oas-raml-converter
git clone https://github.com/mulesoft/oas-raml-converter.git
cd oas-raml-converter
npm run build
cd ..

# Install swagger-to-slate node app
npm i swagger-to-slate
