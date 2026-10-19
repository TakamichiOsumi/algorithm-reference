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
    pass
else:
    # Leave below codes for quick reference.
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = input()
    N = int(input())
    # Ascending order by each 0th element.
    X_Y = [ list(map(int, input().split())) for _ in range(N) ]
    sorted_X_Y = sorted(X_Y, reverse = False, key = lambda x : x[0])

    strings = [ input() for _ in range(N) ]
    chars  = list(input())

    # Q = int(input())
    # for i in range(Q):
    #     s = input()
    #     if s[0] == '1':
    #         q, x, y = map(int, s.split())
    #     else:
    #         q, k = map(int, s.split())
