#!/usr/bin/env ruby
 

puts "### RAML -> OAS20"
puts "git clone git@github.com:mulesoft/oas-raml-converter.git"
puts "npm run build"
puts "./oas-raml-converter/lib/bin/converter.js --from RAML --to OAS20 ./src/product-api-raml/api.raml > ./OAS/api.json"
puts "### OAS -> Slate markup"
puts "npm install -g swagger-to-slate"
puts "swagger-to-slate -i ./OAS/api.json ./slate/"


