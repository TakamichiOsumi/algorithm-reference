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

D, N = map(int, input().split())
period = [24] * (D + 1)
period[0] = 0

for i in range(N):
    L, R, H = map(int, input().split())
    for j in range(L, R + 1):
        period[j] = min(period[j], H)

p(period)
print(sum(period))

