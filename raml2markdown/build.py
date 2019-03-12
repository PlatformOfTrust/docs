#!/usr/bin/env python3

import os
from pathlib import Path
import subprocess

# Array of APIs. Call API_Raml_to_Slate(apiname) for each. Expected: API RAML file in folder which is the api name.
# Inside that folder must be .raml file with the same name. Example: ./src/product-api/product-api.raml
APIs = ["broker-api", "calendar-api", "product-api"]


def api_raml_to_slate(apiname):
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

def concatenate_files():
  outfile = Path("slate/index.html.md")
  if outfile.exists():
    os.remove(outfile)
  else:
    print("File: index.html.md delete failed. File not found!")

  with open(outfile, 'w') as ofile:
    with open(Path("slate/index.md")) as infile:
      ofile.write(infile.read())
    for api in APIs:
      slatefile = Path("./slate/" + api + ".md")

      # Ugly way of getting rid of some markup in the beginning of each file. Get everything after line 18 and
      # save to final markdown file

      ofile.write("# "+api.upper()+"\n")
      infile = open(slatefile, 'r').readlines()
      for index, line in enumerate(infile):
        if index > 18:
          if line.startswith("#"):
            ofile.write("#"+line)
          else:
            ofile.write(line)
  print("\n\nSlate file: "+str(outfile)+" created.")
for api in APIs:
  api_raml_to_slate(api)

concatenate_files()

