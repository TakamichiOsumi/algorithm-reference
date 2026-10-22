#!/usr/bin/env python3

from sortedcontainers import SortedDict # keys, values, items, bisect_left, bisect_right
from sortedcontainers import SortedList # add, bisect_left, bisect_right, count, extend, index, insert(index, value). Note 'del sl[index]' is O(log(n)).
from sortedcontainers import SortedSet # add, remove
from collections import defaultdict # dd = defaultdict(list)
from collections import deque # append, appendleft, extend, extendleft, index, pop, popleft
from collections import Counter # c = Counter('abcdeabc') # ''.join(sorted(c.elements()))) == 'aabbccde'
from itertools import \
    permutations, combinations # permutations(range(A, B)), combinations(range(A, B), C)
from itertools import \
    product, groupby, accumulate # product(range(A, B), range(C, D)), groupby(list(S)), accumulate(A)
import math # math.pow()
import re # for m in re.finditer(r"(aa+)|(bb+)|(cc+)", S): print("Index=", m.start(0), "&", m.end(0), ", String : ", S[ m.start(0) : m.end(0) ])
import sys # sys.setrecursionlimit(10 ** 6)
# from atcoder.segtree import SegTree # seg = SegTree(max, -(10**9), [2, 3, 5, 1, 6]) # set, prod
# from atcoder.dsu import DSU # uf = DSU(int value); # groups, leader, merge, same, size

debug = True # switch
def p(*var):
    if debug:
        if len(var) == 1 and type(var[0]) == type([]):
            print("DEBUG : --dump array--")
            for i in range(len(var[0])):
                print(f"\t{i}:{var[0][i]}")
        else:
            print("DEBUG:", *var)

if __name__ == "__main__":
    N, M = map(int, input().split())
    X_Y = [ list(map(int, input().split())) for _ in range(N) ]
    # Ascending order by each 0th element.
    # sorted_X_Y = sorted(X_Y, reverse = False, key = lambda x : x[0])
    pass
else:
    # Leave below codes for quick reference.
    A = list(map(int, input().split()))
    S = input()
    N = int(input())
    strings = [ input() for _ in range(N) ]
    chars  = list(input())

    # Q = int(input())
    # for i in range(Q):
    #     s = input()
    #     if s[0] == '1':
    #         q, x, y = s.split()
    #     elif s[0] == '2':
    #         q, k = s.split()
    #     elif s[0] == '3':
    #         q, k = s.split()
