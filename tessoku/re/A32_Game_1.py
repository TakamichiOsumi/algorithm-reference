#!/usr/bin/env python3

# This problem can be regarded as DP problem, because "First" win or lose
# can be decided by the number of left stones from 0 to N.
#
# The "First" wins at 'A'th and 'B'th index, which are marked as True around [1].
#
# The iteration at [2] should include 0 to N, all sequential numbers until N.
# I *mistakenly* chose the range(max(A, B) + 1, N + 1), but this can't correctly handle
# the range within the A and B. Imagine the case N= 20, A= 3, B=10. If the loop for [2]
# starts with max(3, 10) + 1 = 11, then, the True/False checks of the internal range
# between 4 to 9 are ignored.
#
# Along with the above logic which starts iteration from 0, 'i - A >= 0' and 'i - B >= 0'
# are required as [3]. Otherwise, the initial iterations like i = 0 lead to minus 'i - A'
# and minus 'i - B' and wrong answers.

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

N, A, B = map(int, input().split())
dp = [False] * (N + 1) # Can create this size, since N <= 10 ** 5.

for i in range(max(A, B) + 1):
    if i == A or i == B:
        dp[i] = True # ....[1]
p("prepared=", dp)

for i in range(N + 1): # ...[2]
    # Must check for both 'i - A >= 0' and 'i - B >= 0' ...[3]
    if (i - A >= 0 and dp[i - A] is False) or (i - B >= 0 and dp[i - B] is False):
        dp[i] = True

p(dp)
print("First" if dp[N] else "Second")
