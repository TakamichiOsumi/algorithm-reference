#!/usr/bin/env python3


# Finding a longest common substring between two strings can be
# converted to a problem of DP with a matrix where each cell gets
# count up when finding a common character during iteration.
#
# As [1] describes, S[i - 1] and T[j - 1] point to 'index - 1' character
# (that starts zero) for both S and T. Always compare the index - 1
# characters between S and T, to create 0-value cells for i==0 and j==0.
#
# The [2] condition picks up bigger value from either the upper cell
# or the left cell, when S[i - 1] != T[j - 1].

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

S = input()
T = input()

edge_counts = [ [0] * (len(T) + 1) # This is row. The size should be T.
                for _ in range(len(S) + 1) ] # This is column. The size should be S.

for i in range(len(S) + 1):
    for j in range(len(T) + 1):
        if i - 1 >= 0 and j - 1 >= 0:
            ary = [edge_counts[i][j - 1],
                   edge_counts[i - 1][j]]
            if S[i - 1] == T[j - 1]: # ... [1]
                edge_counts[i][j] = max(*ary,
                                        edge_counts[i - 1][j - 1] + 1)
            else:
                edge_counts[i][j] = max(*ary) # ...[2]
        elif i - 1 >= 0:
            edge_counts[i][j] = edge_counts[i - 1][j]
        elif j - 1 >= 0:
            edge_counts[i][j] = edge_counts[i][j - 1]

print(edge_counts[len(S)][len(T)])
