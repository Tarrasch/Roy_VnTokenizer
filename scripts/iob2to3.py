#!/usr/bin/env python3
# I (arash) made up a easier to read format iob3

import fileinput

words = []
word = ''
for line_ in fileinput.input():
    line = line_.strip()
    if '\t' not in line:  # End of sentence.
        if words:
            print(' '.join(words))
        print('')  # Print empty lines. signyfing new sentence
        words = []
        continue
    syllable, tag = line.split('\t')
    if tag == 'O':  # Seperator
        if word:
            words.append(word)  # Write current word.
            word = ''
        if words:
            print(' '.join(words))
            words = []
    elif tag == 'B_W':  # Begin word.
        words.append(word)
        word = syllable
    elif tag == 'I_W':  # Inside word.
        word = word + '_' + syllable
