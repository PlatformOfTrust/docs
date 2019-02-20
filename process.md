# Core team on-going API development

Core team develops the APIs. They have own internal processes inside team. 

## API version release

When core team decides to release API version: 

* Commit RAML file(s) in folder to https://github.com/PlatformOfTrust/docs.oftrust.net/tree/master/source/v1/APIs/RAML/  
* Write/update code examples for each API endpoint. Test the code! Samples must work as is eg be complete examples. 
* Provide at least python and curl examples. Write each sample code to separate file. Naming policy ”APIname-method-endpoint”. For example ```productapi-get-products.py```
* Commit example codes as files to https://github.com/PlatformOfTrust/docs.oftrust.net/tree/master/source/v1/APIs/samples/  
* Notify / mark in the roadmap (Trello) that new version is coming out. Add the release date in card


At this point DX team gets involved and hand over from Core Team to DX Team begins. 

# DX team builds the documentation 

At this stage DX team takes over. We use Slate in building the API documentation, but we will not use the Slate for released documentation. Instead we publish documentation as static websites. 

New version release: 

* DX team converts the RAML files to OpenAPI spec files. 
* DX team combines the material in API docs source. For example injects the code examples to correct places in documentation
* DX team tests the code examples, possibly adds more comments 
* DX team reads the docs through, fixes wordings and adds necessary information and links. 
* DX takes care that API docs as a whole is easy to approach and pleasant to use.
 

# New public release

* When the API docs release is built and tested locally, it is committed to Github master. 
* Travis builds the site content the new API docs files in ```build```folder (”bundle exec middleman build”) from master. Resulting folder  contains index.html and needed folders file all files(fonts, images, javascripts and stylesheets)
*  and pushes ```build```folder content to gh-pages branch in Github
* The gh-pages from docs.oftrust.net 

