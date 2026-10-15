
from sortedcontainers import SortedDict
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from collections import defaultdict
from collections import deque
from collections import Counter
import itertools

import numpy
import re

from atcoder.segtree import SegTree
from atcoder.dsu import DSU

import sys

debug = False # switch
def p(*var):
    global debug
    if debug:
        if len(var) == 1 and type(var[0]) == type([]):
            print("DEBUG : --argument array--")
            for i in range(len(var[0])):
                print(f"\t{i}:{var[0][i]}")
        else:
            print("DEBUG:", *var)

N = int(input())
S = input()

pairs = [ (k, list(g)) for k, g in itertools.groupby(S) ]
freqs = [ (t[0], len(t[1])) for t in pairs ]
val = 0
for t in freqs:
    w, d = t
    if w == 'R':
        val = max(val, d)

print(val)
