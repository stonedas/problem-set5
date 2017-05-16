# /usr/bin/env python3

import sys

from collections import Counter

count = 0

hexamer_5 = Counter()
Hexameer_3 = Counter()


for line in open(sys.argv[1]):
    line = line.rstrip()

    if count == 0:
        name = line
        count += 1

    elif count == 1:
        seq = line
        count += 1

    elif count == 2:
        count += 1

    elif count == 3:
        qual = line
        count = 0

        hexamers5 = []
        hexamer5_L = seq[0:6]
        hexa5[hexamer5_L] =+ 1
        hexamers3 = []
        hexamer3_L = seq[-6]
        hexa3[hexamer3_L] += 1

for key, value in hexamer5.items():
    sortme = [(v,k) for k,v in hexamer5.items()]
    sortme
    sortme.sort()
    sortme.reverse()

print("most common 5' hexamer", sortme[0][1])




for key, value in hexamer3.items():
    sortme = [(v,k) for k,v in hexamer3.items()]
    sortme
    sortme.sort()
    sortme.reverse()

print("Most common 3' hexamer", sortme [0][1])
    

