#!/usr/bin/env python3
# I (arash) made up a easier to read format iob3

import fileinput
import codecs
import sys

with codecs.open(sys.argv[1], encoding='utf-8', mode='r', errors='ignore') as f:
    for line_ in f:
        line = line_.strip()
        print(line)
