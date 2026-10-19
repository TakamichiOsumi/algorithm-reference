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
# for m in re.finditer(r"(aa+)|(bb+)|(cc+)", s):
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


def solve(N, sorted_data, K):
    p(sorted_data)
    val = 0

    left = 0
    while left < N:
        right = left + 1
        p("left=", left, ", right=", right)
        while right <= (N - 1) and \
              (sorted_data[right][0] - sorted_data[left][0]) <= K:
            right += 1
        # Get the subset that satisfies the range whose diff are within 'K'.
        sub = sorted_data[left:right]
        p("sub=", sub)

        sorted_BA = sorted(sub, reverse = False, key = lambda x : x[1])

        # Skip the unsatisfactory case.
        if (left - right == 1) and (sorted_data[right][0] - sorted_data[left][0]) > K:
            left = left + 1
            continue

        internal_left = 0
        while internal_left < len(sorted_BA):
            internal_right = internal_left + 1
            ans = 0
            while internal_right <= (len(sorted_BA) - 1) and \
                  (sorted_BA[internal_right][1] - sorted_BA[internal_left][1]) <= K:
                ans += 1
                internal_right += 1
            p("[internal] left=", internal_left, ", right=", internal_right)
            if not ((internal_left - internal_right == 1) and \
               (sorted_BA[internal_right][1] - sorted_BA[internal_left][1] > K)):
                val = max(val, ans + 1)
            internal_left = internal_left + 1

        left = left + 1

    p("return=", val)
    return val

if __name__ == "__main__":
    N, K = map(int, input().split())
    A_B = [ list(map(int, input().split())) for _ in range(N) ]

    if N == 1:
        print(1)
        exit()

    sAB = sorted(A_B, reverse = False, key = lambda x : x[0])
    print(solve(N, sAB, K))
