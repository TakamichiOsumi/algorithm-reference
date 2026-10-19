#!/usr/bin/env python3

import re
# for m in re.finditer(r"(aa+)|(bb+)|(cc+)", s):
#     print("Index=", m.start(0), "&", m.end(0), ", Sub string : ", S[ m.start(0) : m.end(0) ])

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
    S = input()
    if N == 3:
        if S == "BBB" or S == "RRR":
            print("Yes")
        else:
            print("No")
        exit()

    found_sequence = False
    for m in re.finditer(r"(RRR)|(BBB)", S):
        found_sequence = True

    if found_sequence:
        print("Yes")
    else:
        print("No")
