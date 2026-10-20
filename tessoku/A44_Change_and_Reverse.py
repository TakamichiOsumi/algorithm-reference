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
from itertools import permutations, combinations, product, groupby, accumulate
# permutations(range(A, B)), combinations(range(A, B), C)
# product(range(A, B), range(C, D)), groupby(list(S)), accumulate(A), etc
import math
# math.pow()
import numpy
import re
# for m in re.finditer(r"(aa+)|(bb+)|(cc+)", S):
#     print("Index=", m.start(0), "&", m.end(0), ", Sub string : ", S[ m.start(0) : m.end(0) ])

# from atcoder.segtree import SegTree
# seg = SegTree(max, -(10**9), [2, 3, 5, 1, 6]) # set(), prod(), etc
# from atcoder.dsu import DSU
# uf = DSU(int value); # groups(), leader(), merge(), same(), size()

import sys
# sys.setrecursionlimit(10 ** 6) # for recursion.

debug = True # switch
def p(*var):
    global debug
    if debug:
        if len(var) == 1 and type(var[0]) == type([]):
            print("DEBUG : --dump array--")
            for i in range(len(var[0])):
                print(f"\t{i}:{var[0][i]}")
        else:
            print("DEBUG:", *var)

if __name__ == "__main__":
    N, Q = map(int, input().split())
    d = deque(list(range(1, N + 1)))
    reversed = False
    for i in range(Q):
        s = input()
        if s[0] == '1':
            q, x, y = map(int, s.split())
            if not reversed:
                d[x - 1] = y
            else:
                d[N - 1 - (x - 1)] = y
        elif s[0] == '2':
            if not reversed:
                reversed = True
            else:
                reversed = False
        else:
            q, x = map(int, s.split())
            if not reversed:
                print(d[x - 1])
            else:
                print(d[N - 1 - (x - 1)])
        p(d)
