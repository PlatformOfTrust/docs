#!/usr/bin/env python3

import os
from pathlib import Path
import subprocess

# Array of APIs. Call API_Raml_to_Slate(apiname) for each. Expected: API RAML file in folder which is the api name.
# Inside that folder must be .raml file with the same name. Example: ./src/product-api/product-api.raml
APIs = ["broker-api", "calendar-api", "product-api"]


def API_Raml_to_Slate(apiname):
  jsonfile = Path("./OAS/"+apiname+".json")
  slatefile = Path("./slate/"+apiname+".md")

  print("\nConverting "+apiname+" to Slate")

  # Delete previous API docs
  print("Delete previous API doc files")
  if jsonfile.exists():
    os.remove(jsonfile)
  else:
    print("File: "+apiname+".json delete failed. JSON formatted file not found!")

  if slatefile.exists():
    os.remove(slatefile)
  else:
    print("File: "+apiname+".md delete failed. MD formatted file not found!")

  # Generate API docs. First convert RAML -> OpenAPISpec file
  jsoncmd = "./oas-raml-converter/lib/bin/converter.js --from RAML --to OAS20 ./src/" +apiname+ "/" +apiname+ ".raml > ./OAS/"+apiname+".json"
  failure = os.system(jsoncmd)
  if failure:
    print("RAML -> OpenAPISpec failed. Trying next in array.")
  else:
  # Convert from OpenAPISpec to Slate md
    slatecmd= "swagger-to-slate -i ./OAS/" +apiname+ ".json -o ./slate/" +apiname+ ".md"
    failure = os.system(slatecmd)
    if failure:
      print("RAML -> Slate formatted md file creation failed. Trying next in array.")



for api in APIs:
  API_Raml_to_Slate(api)


