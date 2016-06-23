#!/usr/bin/env python3

# Be damn sure to run this with python 3. otherwise .title() will not work with
# unicode

import fileinput

for line_ in fileinput.input():
    line = line_.strip()
    print(line.title())
