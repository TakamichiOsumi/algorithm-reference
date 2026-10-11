#!/usr/bin/env python3

from sortedcontainers import SortedList
from sortedcontainers import SortedDict
from collections import defaultdict

import math

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

A, B = map(int, input().split())
DIV = 1000000007

dd = SortedDict()
dd[0] = 1
dd[1] = A

prev_key = 1
cur_key = 2
while True:
    dd[cur_key] = (dd[prev_key] * dd[prev_key]) % DIV
    p("cur_key", cur_key, "=>", dd[cur_key])
    prev_key = cur_key
    cur_key = cur_key + cur_key
    if cur_key > B:
        p("break with cond=", cur_key, ">", B)
        break
p("created dict=", dd)

val = 1
dict_keys = dd.keys()

while B > 0:

    # Find the maximum key value under (left) B from 'dd'.
    left_keys = [b for b in dict_keys if b <= B]

    max_value = max(left_keys)
    consume = max_value
    
    p("B consumption=", consume ,", multiply", dd[consume])

    # Substract the maximum key from B.
    B -= consume

    # Mltiply the key's value with 'val'.
    val = (val * dd[consume]) % DIV

print(val)
