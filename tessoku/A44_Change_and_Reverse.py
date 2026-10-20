#!/usr/bin/env python3

from collections import deque

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
