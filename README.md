

Getting Started with Docs
------------------------------

[![Build Status](https://travis-ci.org/PlatformOfTrust/docs.svg?branch=master)](https://travis-ci.org/PlatformOfTrust/docs)

### Prerequisites

You're going to need:

 - **Linux or macOS** — Windows may work, but is unsupported.
 - **Ruby, version 2.3.1 or newer**
    - (for macOS) You can use [Homebrew](https://brew.sh/) as the 1st step to install Ruby
    - After Homebrew is installed, install Ruby in the terminal with commans `brew install ruby`
    - Close the current terminal and reopen a new one to proceed with installing bundler.
 - **Bundler** — If Ruby is already installed, but the `bundle` command doesn't work, just run `gem install bundler` in a terminal.
 

### Getting Set Up

1. Clone repository to your hard drive with `git clone git@github.com:PlatformOfTrust/docs.git`
    - in macOS, You may need to add a pair of **public public/private ssh keys** to your **SSH agent**, if you get the following message in the terminal:
    ```
    Warning: Permanently added the RSA host key for IP address '<YOUR IP ADDRESS>' to the list of known hosts.
    Permission denied (publickey).
    fatal: Could not read from remote repository.
    ```
    Follow [these instructions](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent) to generate the SSH key pairs. Follow [these instructions](https://help.github.com/en/articles/adding-a-new-ssh-key-to-your-github-account) to add them in your GitHub user account

    Please make sure you have the correct access rights
    and the repository exists.

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
2. npm install
3. rm -rf ./oas-raml-converter
4. git clone https://github.com/mulesoft/oas-raml-converter.git
5. cd oas-raml-converter
6. npm install
7. npm run build

**build the docs:**
1. Just add RAML to specific folder (https://github.com/PlatformOfTrust/docs/tree/master/raml2markdown/src),
2. Generate code examples (https://github.com/PlatformOfTrust/code-examples-generator/tree/master/doc)
3. Validate code examples (https://github.com/PlatformOfTrust/code-examples-validator)
4. Set generated code examples path e.g. `export CODE_EXAMPLES="../code-examples"`
5. then run `build.py` and 
6. new docs is generated to https://github.com/PlatformOfTrust/docs/tree/master/build
