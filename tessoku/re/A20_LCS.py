#!/usr/bin/env python3

from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from collections import defaultdict
from collections import deque
from collections import Counter
import itertools
import math
import numpy
import re
from atcoder.segtree import SegTree
from atcoder.dsu import DSU
import sys

debug = True # switch
def p(*var):
    global debug
    if debug:
        if len(var) == 1 and type(var[0]) == type([]):
            print("DEBUG : --argument array--")
            for i in range(len(var[0])):
                print(f"\t{i}:{var[0][i]}")
        else:
            print("DEBUG:", *var)

S = input()
T = input()

# ... [3]
edge_counts = [ [0] * 2001 for _ in range(2001) ]

for i in range(len(S) + 1):
    for j in range(len(T) + 1):
        if i - 1 >= 0 and j - 1 >= 0 and S[i - 1] == T[j - 1]: # ... [1]
            edge_counts[i][j] = max(edge_counts[i - 1][j - 1] + 1,
                                    edge_counts[i][j - 1],
                                    edge_counts[i - 1][j])
        elif i - 1 >= 0 and j - 1 >= 0: # ... [2]
            edge_counts[i][j] = max(edge_counts[i][j - 1],
                                    edge_counts[i - 1][j])
        elif i - 1 >= 0:
            edge_counts[i][j] = edge_counts[i - 1][j]
        elif j - 1 >= 0:
            edge_counts[i][j] = edge_counts[i][j - 1]
        else:
            edge_counts[i][j] = 0

print(edge_counts[len(S)][len(T)])
