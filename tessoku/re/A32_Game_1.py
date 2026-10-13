#!/usr/bin/env python3

from sortedcontainers import SortedDict
# keys(), values(), items(), bisect_left(), bisect_right(), etc
from sortedcontainers import SortedList
# add(), bisect_left(), bisect_right(), count(), extend(), index(), insert(index, value), etc
from sortedcontainers import SortedSet
# add(), remove(), etc
from collections import defaultdict
# dd = defaultdict(list)
from collections import deque
# append(), appendleft(), extend(), extendleft(), index(), pop(), popleft(), etc
from collections import Counter
# c = Counter('abcdeabc') # ''.join(sorted(c.elements()))) == 'aabbccde'
import itertools
# itertools.permutations(range(A, B)), itertools.combinations(range(A, B), C)
# itertools.product(range(A, B), range(C, D)), itertools.groupby(list(S))
# itertools.accumulate(A), etc
import math
# math.pow()
import numpy
import re
# for m in re.finditer(r"(aa+)|(bb+)|(cc+)", s):

from atcoder.segtree import SegTree
# seg = SegTree(max, -(10**9), [2, 3, 5, 1, 6]) # set(), prod(), etc
from atcoder.dsu import DSU
# uf = DSU(int value); # groups(), leader(), merge(), same(), size()

import sys
# sys.setrecursionlimit(10 ** 6) # for recursion.

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

N, A, B = map(int, input().split())
dp = [False] * (N + 1)

for i in range(max(A, B) + 1):
    if i == A or i == B:
        dp[i] = True
p("prepared=", dp)

for i in range(N + 1):
    # Checks for both 'i - A >= 0' and 'i - B >= 0' are must.
    if (i - A >= 0 and dp[i - A] is False) or (i - B >= 0 and dp[i - B] is False):
        dp[i] = True

p(dp)
print("First" if dp[N] else "Second")
