

Getting Started with Docs
------------------------------

### Prerequisites

You're going to need:

 - **Linux or macOS** — Windows may work, but is unsupported.
 - **Ruby, version 2.3.1 or newer**
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

### Build distribution

Python script `raml2markdown/build.py` builds the documentation to `build` folder as static html content with CSS and other necessary files. 
