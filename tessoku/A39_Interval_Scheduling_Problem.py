#!/usr/bin/env python3

# Key Takeaways:
#
# This is a well-known (typical) problem called "interval scheduling"
# which can be solved by "greedy algorithm".
#
# The core logic is to focus on and select the movie whose 'R' time
# is earliest throughout 'L', 'R' pairs iteration.
#
# The [1] part makes it easy to find the movie that ends first in
# the deque. Also, the part [2] skips the overlapped movies that
# can be ignored.

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
    N = int(input())
    L_R = [ list(map(int, input().split())) for _ in range(N) ]

    # Sort by early 'R' time.
    d = deque(sorted(L_R, reverse = False, key = lambda x : x[1])) # .... [1]
    d_idx = 0

    ans = 0
    while len(d) > 0:
        # Pick up the next movie to end first at this moment.
        L, R = d[d_idx][0], d[d_idx][1]
        # Then, discard all movies that starts before the 'R'.
        # 'L' that starts before the 'R' means the overlapping
        # of time with the current chosen movie, d[d_idx].
        while len(d) > 0 and d[0][0] < R: # .... [2]
            d.popleft()
        # The above logic can be regarded as selection of one movie.
        ans += 1

    print(ans)
