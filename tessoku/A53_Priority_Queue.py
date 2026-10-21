#!/usr/bin/env python3

from sortedcontainers import SortedList

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
    products = SortedList([])
    for i in range(Q):
        s = input()
        if s[0] == '1':
            q, x = map(int, s.split())
            products.add(x)
        elif s[0] == '2':
            print(products[0])
        elif s[0] == '3':
            # According to the python library manual,
            # the runtime cpmplexity of 'del sl[index]' is O(log(n)).
            del products[0]
