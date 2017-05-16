#/usr/bin/env python3 

import sys

from collections import Counter
from pysam import AlignmentFile

count = 0
strands = Counter()
mismatch = Counter()

bamfile = AlignmentFile(sys.argv[1])

for record in bamfile:
    strand = record.flag
    strands[strand] += 1
for strand, count in strands.items():
    if strand == 0:
        print("positve strand allignments", count)
    if strand == 16:
        print("negative strand alignments", count)

for record in bamfile:
    nm = record.get_tag('NM')
    mismatch[NM] += 1
for nm, count in mismatch.items():
    if nm == 0:
        print("Total # of alignments without mismatches", count)
    elif nm != 0:
        global counts
        counts += count
        print("total # of alignments with greater than 0 mismatches",
        counts)
