#!/usr/bin/env python3

from collections import Counter

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
    N = int(input())
    A = list(map(int, input().split()))
    A = Counter(A)
    p(A)
    ans = 0
    for length, number in A.items():
        if number >= 3:
            ans += (number * (number - 1) * (number - 2)) // 6
    print(ans)
