#!/usr/bin/env python3

from sortedcontainers import SortedDict # keys, values, items, bisect_left, bisect_right

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
    sd = SortedDict()
    for i in range(Q):
        s = input()
        if s[0] == '1':
            op, person, score = s.split()
            sd[person] = int(score)
        elif s[0] == '2':
            op, person = s.split()
            print(sd[person])
        elif s[0] == '3':
            pass
