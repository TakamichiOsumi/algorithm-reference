#!/usr/bin/env python3

"""
Referred to https://github.com/TakamichiOsumi/algorithm-reference.
"""

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
            print("DEBUG : --dump array--")
            for i in range(len(var[0])):
                print(f"\t{i}:{var[0][i]}")
        else:
            print("DEBUG:", *var)

N, M = map(int, input().split())
A = list(map(int, input().split()))
S = input()
N = int(input())
X_Y = [ list(map(int, input().split())) for _ in range(N) ]

# # Ascending order by each 0th element.
# sorted_X_Y = sorted(X_Y, reverse = False, key = lambda x : x[0])
# strings = [ input() for _ in range(N) ]
# chars  = list(input())
# Q = int(input())
# for i in range(Q):
#     s = input()
#     if s[0] == '1':
#         # query = 1
#         q, x, y = map(int, s.split())
#     else:
#         # other cases like for query = 2.
#         q, k = map(int, s.split())

