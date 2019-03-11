#!/bin/sh

clear

# Convert Product API RAML to Slate format
echo "\n\nProduct API to Slate"

echo "Delete previous product API files"
rm ./OAS/product-api.json
rm ./slate/product-api.md
./oas-raml-converter/lib/bin/converter.js --from RAML --to OAS20 ./src/product-api/product-api.raml > ./OAS/product-api.json
swagger-to-slate -i ./OAS/product-api.json -o ./slate/product-api.md

if [ ! -f ./slate/product-api.md ]; then
    echo "Product API Slate doc not created!"
    exit
fi
echo "PRODUCT API SLATE CREATED"
ls -al ./slate/product-api.md
echo "\n\n"


# Convert Context API RAML to Slate formatˍ
echo "Context API to Slate"

echo "Delete previous Context API files"
rm ./OAS/context-api.json
rm ./slate/context-api.md
./oas-raml-converter/lib/bin/converter.js --from RAML --to OAS20 ./src/context-api/context-api.raml > ./OAS/context-api.json
swagger-to-slate -i ./OAS/context-api.json -o ./slate/context-api.md

if [ ! -f ./slate/context-api.md ]; then
    echo "Context API Slate doc not created!"
    exit
fi
echo "CONTEXT API SLATE CREATED"
ls -al ./slate/context-api.md
