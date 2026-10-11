#!/usr/bin/env python3

# Key Takeaways:
#
# (1) For '+', '-' and '*', timing to calculate '%' doesn't affect
#     the calculation result like [1], [2] and [3].
#
# (2) The next key for 'dd' is 'cur_key + cur_key' as described in [4].
#     This is because the dictionary key is the number of total multiplied
#     times of A, the exponent of A. Thus, the key is calculated by '+'.

from sortedcontainers import SortedList
from sortedcontainers import SortedDict
from collections import defaultdict

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
    dd[cur_key] = (dd[prev_key] * dd[prev_key]) % DIV # ... [1]
    p("cur_key", cur_key, "=>", dd[cur_key])
    prev_key = cur_key
    cur_key = cur_key + cur_key # ... [4]
    if cur_key > B:
        p("break with cond=", cur_key, ">", B)
        break
p("created dict=", dd)

val = 1
dict_keys = dd.keys()

while B > 0:

    # Find the maximum key value under (left) B from 'dd'.
    left_keys = [b for b in dict_keys if b <= B]

    consume = max(left_keys)
    p("B consumption=", consume ,", multiply", dd[consume])
    # Substract the maximum key from B.
    B -= consume

    # Mltiply the key's value with 'val'.
    val = (val * dd[consume]) % DIV # ... [2]

print(val) # ... [3]
