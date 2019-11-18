#!/usr/bin/env python3

import os
import re
import shutil
import sys
from pathlib import Path

# Array of APIs. Call API_Raml_to_Slate(apiname) for each. Expected: API RAML file in
# folder which is the api name.
# Inside that folder must be .raml file with the same name. Example:
# ./src/product-api/product-api.raml
APIs = [
  "ACL-api",
  "Application-api",
  "Broker-api",
  "Calendar-api",
  "Context-api",
  "Identity-api",
  "Login-api",
  "Message-api",
  "Product-api"
]

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
    local_swagger_to_slate = "./node_modules/.bin/swagger-to-slate"
    swagger_to_slate = local_swagger_to_slate if os.path.exists(local_swagger_to_slate) else "swagger-to-slate"
    slatecmd = swagger_to_slate + " -i ./OAS/" + apiname + ".json -o ./slate/" + apiname + ".md"
    failure = os.system(slatecmd)
    if failure:
      print("RAML -> Slate formatted md file creation failed. Trying next in array.")


# Generate path according to code examples location pattern:
# https://github.com/PlatformOfTrust/code-examples-generator/tree/master/doc#4-code-example-location
def get_generated_code_examples_path(root, line, api):
  line = line.rstrip(os.linesep)
  line = re.sub('[`*]', '', line)
  line_arr = line.split(' ')
  # parse HTTP method
  method = line_arr[0]
  # convert forward slashes to underscores to match code examples file path
  if len(line_arr) > 1 :
    filename = re.sub('[/]', '_', line_arr[1])
  else:
    filename = ''

  #print('/'.join([root, api, api + ".raml", filename, method, "slate.md"]))
  return Path('/'.join([root, api, api + ".raml", filename, method, "slate.md"]))

def concatenate_files(code_examples_path):
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

      ofile.write("# " + api.replace("-", " ").replace("api", "") + "\n")
      pretty_api_name = api.replace("-", " ").replace("api", "API")

      ofile.write("\n> **Get "+pretty_api_name+ " related resources:**\n\n")
      # ofile.write("> - <div class='oas-spec-file'><a href='./specs/oas/"+api.lower()+".json'>Open API Specification (JSON)</a>\n\n")
      # ofile.write("\n")
      # ofile.write("> - <div class='raml-spec-file'><a href='./specs/raml/" + api.lower() + ".zip'>RAML Specification (zip)</a>\n\n")
      # ofile.write("\n\n")
      # ofile.write(" > <div class='raml-spec-file'><a href='./specs/raml/"+api.lower()+".zip'>RAML Spec (zip)</a></div>")

      ofile.write("> <div class='hexagon'><div class='hexagon-inside'><div class='hexagon-inside2'>")
      ofile.write("<a href='./specs/oas/"+ api.lower() + ".json' title='Get OpenAPI Specification Resources'>")
      ofile.write("<img src='images/oas.png' class='openApiSpec-lg'>")
      ofile.write("</a></div></div></div>")
      ofile.write("\n")
      ofile.write("> <div class='hexagon'><div class='hexagon-inside'><div class='hexagon-inside2'>")
      ofile.write("<a href='./specs/raml/"+ api.lower() + ".zip' title='Get RAML Specification Resources'>")
      ofile.write("<img src='images/raml.png' class='ramlSpec-lg'>")
      ofile.write("</a></div></div></div>")
      ofile.write("\n\n")

      infile = open(slatefile, 'r').readlines()
      for index, line in enumerate(infile):

        # Now match the lines after which the code examples are injected.
        # example of one line: `***PUT*** /products/{product_code}`
        # That should match product-api_PUT_product_code.curl in examples folder
        # example_file= str(line)
        copyline = str(line)
        # example_file = example_file.rstrip(os.linesep)
        # example_file = re.sub('[`#* {}]', '', example_file)
        # example_file = re.sub('//', '_', example_file)
        # example_file = re.sub('[/]', '_', example_file)
        # example_file = re.sub('I', 'i', example_file)

        example_method = str(line)
        example_method = re.sub('[`#*]', '', example_method)

        #example_file_path = Path("./examples/" +api.lower() +"_"+ example_file + ".md")
        example_file_path = get_generated_code_examples_path(
          code_examples_path,
          str(line),
          api.lower()
        )

        example_desc = "\n\n > <b>Example for: "+example_method.replace("{version}","v1")+"</b>\n\n"
        if len(str(example_file_path)) < 200:
          if example_file_path.exists():
            with open(example_file_path) as sfile:
              print("Found example file: " + str(example_file_path) +" derived from line:" + copyline)
              ofile.write("> <div class='hexagon-so'><div class='hexagon-inside-so'><div class='hexagon-inside2-so'><p>Do you need help in using the "+example_method.replace("{version}","v1")+"? </p>")
              ofile.write("<li><a href='https://stackoverflow.com/questions/tagged/platform-of-trust' title='Check out Platform of Trust questions and answers in Stack Overflow' target='new'>Checkout existing questions & answers</a></li>")
              ofile.write("<li><a href='https://stackoverflow.com/questions/ask?guided=false&tags=platform-of-trust,"+api.lower()+"' title='Ask a question in Stack Overflow' target='new'>Ask a question in Stack Overflow</a></li>")
              ofile.write("</br>")
              ofile.write(
                "<li><a href='https://github.com/PlatformOfTrust/docs/issues/new?assignees=&template=i-m-in-pain--here-s-the-symptoms.md&title=Customer+wish&labels="+ api.lower()+",Wish' title='Make a wish!' target='new'>Did we miss something? Make a wish!</a></li>")
              # ofile.write("<img src='images/raml.png' class='ramlSpec-lg'>")
              ofile.write("<div style='min-height:30px;'>&nbsp;</div>")
              ofile.write("</div></div></div>")
              ofile.write("\n\n")
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

  # Make zips for RAML in the build folder /build/specs/raml.
  ramlpath = "../build/specs/raml"
  try:
    os.makedirs(ramlpath)
  except OSError:
    print("Creation of the directory %s failed" % path)
  else:
    print("Successfully created the directory %s" % path)
    for api in APIs:
      apiname = api.lower()
      src_path = "./src/" + apiname
      shutil.make_archive(ramlpath+"/"+apiname, 'zip', src_path)

# ----------------------------
# MAIN - lets build it

code_examples_var = 'CODE_EXAMPLES'

# Make sure that code example source has been passed
try:
   os.environ[code_examples_var]
except KeyError:
   print("Please set the environment variable " + code_examples_var)
   sys.exit(1)

# Generate content
for api in APIs:
  api_raml_to_slate(api)

# Merge all together
concatenate_files(os.environ[code_examples_var])

# Build deployable content as html
make_html()

# copy the RAMLs and OAS spec files to build
copy_specs_to_build()
