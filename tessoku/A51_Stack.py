#!/usr/bin/env python3

from collections import deque

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
    Q = int(input())
    d = deque([])
    for i in range(Q):
        s = input()
        if s[0] == '1':
            q, x = s.split()
            d.appendleft(x)
        elif s[0] == '2':
            print(d[0])
        elif s[0] == '3':
            d.popleft()
