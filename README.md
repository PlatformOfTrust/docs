

Getting Started with Docs
------------------------------

### Prerequisites

You're going to need:

 - **Linux or macOS** — Windows may work, but is unsupported.
 - **Ruby, version 2.3.1 or newer**
    - (for macOS) You can use [Homebrew](https://brew.sh/) as the 1st step to install Ruby
    - After Homebrew is installed, install Ruby in the terminal with commans `brew install ruby`
 - **Bundler** — If Ruby is already installed, but the `bundle` command doesn't work, just run `gem install bundler` in a terminal.

### Getting Set Up

1. Clone repository to your hard drive with `git clone git@github.com:PlatformOfTrust/docs.git`
2. `cd docs`
3. Initialize and start Platform of Trust API Docs: 

```shell
bundle install
bundle exec middleman server

```

You can now see the docs at http://localhost:4567. 

### Rebuild API Docs

The current documentation is fully automated at the moment (except writing the code examples). 

**build needed tools:**
1. cd raml2markdown
2. rm -rf ./oas-raml-converter
3. git clone https://github.com/mulesoft/oas-raml-converter.git
4. cd oas-raml-converter
5. npm install
6. npm run build
7. npm i -g swagger-to-slate

**build the docs:**
1.	Just add RAML to specific folder (https://github.com/PlatformOfTrust/docs/tree/master/raml2markdown/src),  
2.	Add code examples (https://github.com/PlatformOfTrust/docs/tree/master/raml2markdown/examples), 
3.	then run `build.py` and 
4.	new docs is generated to https://github.com/PlatformOfTrust/docs/tree/master/build
