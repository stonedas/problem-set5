#! /usr/bin/env python3

from collections import Counter

counts = Counter()

import sys

for line in open(sys.argv[1]):
    if line.startswith('#'): continue
    fields = line.split('\t')
    chrom = fields[0]
    counts[chrom] += 1

for chrom, count in counts.items():
    sortme = [(v,k) for k,v in counts.items()]
    sortme
    sortme.sort()
    sortme.reverse()
print(sortme[0][1])


