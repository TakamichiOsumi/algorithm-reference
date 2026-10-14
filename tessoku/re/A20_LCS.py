#!/usr/bin/env python3


# Finding a longest common substring between two strings can be
# converted to a problem of DP with a matrix where each cell gets
# count up when finding a common character during iteration.
#
# As [1] describes, S[i - 1] and T[j - 1] point to 'index - 1' character
# for both S and T. Always compare the index - 1 characters between
# S and T, to create 0 values cells for i==0 and j==0.
#
# The [2] condition picks up bigger value from either the upper cell
# or the left cell, when S[i - 1] != T[j - 1].
#
# Allocate enough memory for the matrix in [3].

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

# ... [3]
edge_counts = [ [0] * 2001 for _ in range(2001) ]

for i in range(len(S) + 1):
    for j in range(len(T) + 1):
        if i - 1 >= 0 and j - 1 >= 0 and S[i - 1] == T[j - 1]: # ... [1]
            edge_counts[i][j] = max(edge_counts[i - 1][j - 1] + 1,
                                    edge_counts[i][j - 1],
                                    edge_counts[i - 1][j])
        elif i - 1 >= 0 and j - 1 >= 0: # ... [2]
            edge_counts[i][j] = max(edge_counts[i][j - 1],
                                    edge_counts[i - 1][j])
        elif i - 1 >= 0:
            edge_counts[i][j] = edge_counts[i - 1][j]
        elif j - 1 >= 0:
            edge_counts[i][j] = edge_counts[i][j - 1]

print(edge_counts[len(S)][len(T)])
