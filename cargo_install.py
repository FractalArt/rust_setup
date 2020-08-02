#!/usr/bin/env python3

import subprocess as sp
import sys

packages = [
    'ripgrep',
    'fd-find',
    'bat',
    'exa',
    'hyperfine',
    'cargo-license',
    'diskus',
    'du-dust',
    'emulsion',
    'tokei', # can also be installed with `cargo install tokei --features all`
    'diskonaut',
    'cargo-lichking',
    'cargo-tree',
    'cargo-deps',
    'procs',
    'ytop',
]

for package in packages:
    print(f"Installing: {package}...")
    pack_ret = sp.call(['cargo', 'install', '--force', package])
    if pack_ret != 0:
        print("--- Error!")
    else:
        print("--- Done!")

# Blindfold can so far not be installed by simple cargo install Blindfold
# Github URL: https://github.com/Eoin-McMahon/Blindfold.git
print(f"--- The package `Blindfold needs to be installed by hand.`")
