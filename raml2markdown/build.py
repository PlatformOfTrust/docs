#!/usr/bin/env python3

import os
import re
from pathlib import Path
import shutil

import subprocess

# Array of APIs. Call API_Raml_to_Slate(apiname) for each. Expected: API RAML file in folder which is the api name.
# Inside that folder must be .raml file with the same name. Example: ./src/product-api/product-api.raml
APIs = ["Broker-api", "Calendar-api", "Context-api", "Identity-api", "Message-api", "Product-api"]


def api_raml_to_slate(apiname):
  apiname = apiname.lower()
  jsonfile = Path("./OAS/"+apiname+".json")
  slatefile = Path("./slate/"+apiname.lower()+".md")

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
  outfile = Path("../source/index.html.md")
  if outfile.exists():
    os.remove(outfile)
  else:
    print("File: index.html.md delete failed. File not found!")

  with open(outfile, 'w') as ofile:
    with open(Path("slate/index.md")) as infile:
      ofile.write(infile.read())
    for api in APIs:
      slatefile = Path("./slate/" + api.lower() + ".md")

      ofile.write("# " + api.replace("-", " ").replace("api", "API") + "\n")

      ofile.write("\n> **Download API specification:**\n\n")
      ofile.write("> - <div class='oas-spec-file'><a href='./specs/oas/"+api.lower()+".json'>Open API Spec (JSON)</a>\n\n")
      ofile.write("\n\n")
      # ofile.write(" > <div class='raml-spec-file'><a href='./specs/raml/"+api.lower()+".zip'>RAML Spec (zip)</a></div>")



      infile = open(slatefile, 'r').readlines()
      for index, line in enumerate(infile):

        # Now match the lines after which the code examples are injected.
        # example of one line: `***PUT*** /products/{product_code}`
        # That should match product-api_PUT_product_code.curl in examples folder
        example_file= str(line)
        copyline = str(line)
        example_file = example_file.rstrip(os.linesep)
        example_file = re.sub('[`#* {}]', '', example_file)
        example_file = re.sub('//', '_', example_file)
        example_file = re.sub('[/]', '_', example_file)
        example_file = re.sub('I', 'i', example_file)

        example_file_path = Path("./examples/" +api.lower() +"_"+ example_file + ".md")

        example_method = str(line)
        example_method = re.sub('[`#*]', '', example_method)

        example_desc = "\n\n > <b>Example for: "+example_method.replace("{version}","v1")+"</b>\n\n"
        if len(str(example_file_path)) < 200:
          if example_file_path.exists():
            with open(example_file_path) as sfile:
              print("Found example file: " + str(example_file_path) +" derived from line:" + copyline)
              ofile.write(example_desc)
              ofile.write(sfile.read()+"\n\n")


        # Ugly way of getting rid of some markup in the beginning of each file. Get everything after line 18 and
        # save to final markdown file
        if index > 18:
          # Some markdown cleanup since the converters mess things up
          if line.startswith("#"):
            ofile.write("#"+line.lower().replace("***", "**").replace("{version}","v1"))
          elif line.startswith("`***"):
            ofile.write(line.replace("***", "**").replace("`", "").replace("{version}","v1"))
          else:
            ofile.write(line.replace("***", "**").replace("{version}","v1"))
  print("\n\nSlate file: "+str(outfile)+" created.")


def make_html():
  cmd = "cd .. & bundle exec middleman build"
  failure = os.system(cmd)
  if failure:
    print("HTML build failed")
  else:
    print("\n\nHTML generated successfully.")


def copy_specs_to_build():
  #make directory
  # define the name of the directory to be created
  path = "../build/specs/oas"

  try:
    os.makedirs(path)
  except OSError:
    print("Creation of the directory %s failed" % path)
  else:
    print("Successfully created the directory %s" % path)
    # Copy oas spec file to build release as well
    for api in APIs:
      apiname = api.lower()
      src_path = "./OAS/" + apiname + ".json"
      shutil.copy2(src_path, '../build/specs/oas')  # target filename  preserved

# ----------------------------
# MAIN - lets build it

# Generate content
for api in APIs:
  api_raml_to_slate(api)

# Merge all together
concatenate_files()

# Build deployable content as html
make_html()

# copy the RAMLs and OAS spec files to build
copy_specs_to_build()
