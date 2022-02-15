#!/usr/bin/env python
# mapper - we are going to break the sentences into tokens or units

import sys
import re
# stdin - standard input
for line in sys.stdin:
    
    # strip white spaces at the beggining and end of line
    line = line.strip()

    # split each line into words
    # using regular expressions splitting punctuations from word
    words = re.findall(r"[A-Za-z]+|\S",line.strip())
    words = [i.lower() for i in words]
    
    #process each word and assign a value of 1 to each word    
    for i in words:
        print(i + "\t1")

