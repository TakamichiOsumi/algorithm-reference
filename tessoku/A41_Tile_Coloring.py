#!/usr/bin/env python3

# This problem can be solved by an idea that
# appending 'R' or 'B' to edges of one sequence of 'RRR' or 'BBB'.
# Therefore, finding one sequence of either 'RRR' and 'BBB' is confident
# enough to judge the result.

import re

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
