

Getting Started with Docs
------------------------------

### Prerequisites

You're going to need:

 - **Linux or macOS** — Windows may work, but is unsupported.
 - **Ruby, version 2.3.1 or newer**
 - **Bundler** — If Ruby is already installed, but the `bundle` command doesn't work, just run `gem install bundler` in a terminal.

### Getting Set Up

1. Fork this repository on GitHub.
2. Clone *your forked repository* (not our original one) to your hard drive with `git@github.com:PlatformOfTrust/docs.git`
3. `cd docs`
4. Initialize and start Platform of Trust API Docs. 

```shell
bundle install
bundle exec middleman server

```

You can now see the docs at http://localhost:4567. 

### Build distribution

To build distribution content, use ```bundle exec middleman build``` and static content to serve via webserver is in ```build``` folder. 
