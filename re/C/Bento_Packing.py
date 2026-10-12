#!/usr/bin/env python3

from sortedcontainers import SortedDict
from sortedcontainers import SortedList

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

N, W = map(int, input().split())

A_B = SortedList([])
for _ in range(N):
    A, B = list(map(int, input().split()))
    A_B.add(list([B, A]))

p(A_B)

def bit_brute_force_patterns(N):
    combinations = []
    for i in range(2 ** N):
        ary = []
        for j in range(N):
            if ((i >> j) & 1):
                ary.append(j)
        combinations.append(ary)

    return combinations

leave_indexes = lambda items, indexes: [item for index, item in enumerate(items) if index in indexes]

res = 0
patterns = bit_brute_force_patterns(N)
for pattern in patterns:
    if len(pattern) == 0:
        continue
    left = leave_indexes(A_B, pattern)
    p(left)
    cur_taste = cur_weight = 0
    for item in left:
        cur_weight += item[0]
        cur_taste += item[1]

    if cur_weight <= W:
        res = max(res, cur_taste)

print(res)

