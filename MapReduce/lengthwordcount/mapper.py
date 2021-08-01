"""
@Author: Ranjith G C
@Date: 2021-07-28
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-28 
@Title : Program Aim is to work with length of each word count using mapper.
"""

#!/usr/bin/env python
  
# import sys because we need to read and write data to STDIN and STDOUT
import sys
  
# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
      
    # we are looping over the words array and printing the word
    # with the count of 1 to the STDOUT
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
	print("%s\t%s" % (len(word), 1))
