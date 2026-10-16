#!/usr/bin/env python3

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

N, K = map(int, input().split())

if K < (N - 1) * 2:
    print("No")
else:
    v = K - ((N - 1) * 2)
    if v % 2 == 0:
        print("Yes")
    else:
        print("No")
