#!/usr/bin/env python
# coding: utf-8

# In[1]:

import numpy as np


MIN_HITS = 2
MIN_BASES = 4
BASES = ['A', 'C', 'G', 'T']


# returns the amount of hits in a given string
def hitscount(line: str) -> int:
    count = 0
    for base in BASES:
        count += line.count(base*MIN_BASES)
    return count


# receives a DNA sample and returns True if it's Metahuman or False
def ismeta(dna) -> bool:

    dna_arr = np.array([list(line) for line in dna])
    dna_arr_t = np.fliplr(dna_arr)

    n = len(dna)
    hits = 0

    # A hit consists of 4 bases, any less than 4 is a human
    if n < MIN_BASES:
        return False

    else:
        # Check horizontally
        rows = ".".join(dna)
        hits += hitscount(rows)

        # Check vertically
        columns = ".".join(list(map(''.join, zip(*dna))))
        hits += hitscount(columns)

        # Check diagonally
        # first 3 rows won't have enough characters for a hit
        cant_diag = n - MIN_BASES - 1

        diags = "".join(dna_arr.diagonal())+"."+"".join(dna_arr_t.diagonal())

        # cant add to the array because all different size
        for i in range(1, cant_diag):
            upper = "".join(dna_arr.diagonal(i))
            lower = "".join(dna_arr.diagonal(-i))
            upper_t = "".join(dna_arr_t.diagonal(i))
            lower_t = "".join(dna_arr_t.diagonal(-i))

            diags = ".".join([diags, upper, lower, upper_t, lower_t])

        hits += hitscount(diags)

        # Checks if the amount of hits has reached the min hits required
        return hits >= MIN_HITS

# In[ ]:
