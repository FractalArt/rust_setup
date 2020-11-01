#!/usr/bin/env python3

# Also look at: https://zaiste.net/posts/shell-commands-rust/

import subprocess as sp
import sys

packages = [
    'ripgrep',
    'fd-find',
    'bat',
    'exa',
    'hyperfine',
    'cargo-license',
    #'diskus',
    'du-dust',
    'emulsion',
    'tokei', # can also be installed with `cargo install tokei --features all`
    'diskonaut',
    'cargo-lichking',
    'cargo-deps',
    'procs',
    'ytop',
    'sd', # Nice to perform replacements in many files.
    'grex', # create regexes from examples
    'blindfold', # gitignore files
    'starship',
    'mdbook',
    'lfs',
    #  sudo apt install libncurses5 libncurses5-dev libncursesw5 libncursesw5-dev
    #cargo install --git https://github.com/adder46/hstr-rs.git
]

for package in packages:
    print(f"Installing: {package}...")
    pack_ret = sp.call(['cargo', 'install', '--force', package])
    if pack_ret != 0:
        print("--- Error!")
    else:
        print("--- Done!")
