#!/usr/bin/env python3

import fileinput
import re

word = ''
for line_ in fileinput.input():
    line = line_.strip()
    if re.search('##', line):
        for word_ in line.split(','):
            word = word_.strip()
            word = re.sub('##', '', word)
            word = re.sub(' ', '_', word)
            print(word)
