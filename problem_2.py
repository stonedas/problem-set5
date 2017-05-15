#! usr/bin/env python3

from collections import Counter
count = 0
bases = Counter

import sys
filename = sys.argv[1]

for line in open(~/data-sets/fastq/SP1.fq):
    line = line.rstrip()
    if count == 0
        name = line
        count += 1
    elif count == 1
        seq = line
        count += 1
    elif count == 2
        count += 1

    for base in seq:
        bases(base) += 1 
