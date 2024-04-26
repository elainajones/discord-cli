# README

## About

Currently a simple Python demo for getting Discord content from the CLI.

THis is a work in progress and is subject to change.

## Usage

1. `git clone https://www.github.com/elainajones/discord-cli.git`
2. `cd discord-cli`
3. `make install`
4. `. .venv/bin/activate`
5. Add the following to `.env` (**note:** this is NOT tracked by git or shared)
    - `LOGIN='<YOUR DISCORD EMAIL HERE>'`
    - `PASSWORD='<YOUR DISCORD PASSWORD HERE>'`

Once done, you can run the example `discord.py` code. This will return a list of guilds (also known as servers) that you're a member of as well as their corresponding ID which will be needed for additional requests.
