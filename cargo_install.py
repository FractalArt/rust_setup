#!/usr/bin/env python3

import subprocess as sp
import sys

packages = [
    'ripgrep',
    'fd-find',
    'bat',
    'exa',
    'hyperfine'
]

for package in packages:
    print(f"Installing: {package}...")
    pack_ret = sp.call(['cargo', 'install', '--force', package])
    if pack_ret != 0:
        print("--- Error!")
    else:
        print("--- Done!")
