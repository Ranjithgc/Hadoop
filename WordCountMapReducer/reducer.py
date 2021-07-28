#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    word,count = line.split('\t')

    # convert count (currently a string) to int
    count = int(count)
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word
# for printing the last word
if current_word == word:
    print('%s\t%s' % (current_word, current_count))

