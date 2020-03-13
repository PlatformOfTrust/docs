#!/usr/bin/env bash 
set -exuo pipefail

git clone https://github.com/PlatformOfTrust/api-docs-product.git

cd CodeGen-Code
npm install

cp -r doc-generation/lib ./docs/raml2markdown/oas-raml-converter/

cd docs
bundle install

cd raml2markdown
npm install
npm install swagger-to-slate

cd ../..

cp -r doc-generation/src ./docs/raml2markdown/node_modules/swagger-to-slate

mkdir resources/Temp-Files

node API-Engine-cmd.js --input ../raml2markdown/src --output ../ --host $HOST --scheme $SCHEME