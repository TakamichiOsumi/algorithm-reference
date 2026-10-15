#!/usr/bin/env python3

# TODO: Complete this problem. Not finished yet.

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

N = int(input())
dp = [ [0] * (N) for _ in range(N + 1) ]

# P_A = [ list(map(int, input().split())) for _ in range(N) ]
# P_A = [ [P_A[i][0] - 1, P_A[i][1]] for i in range(N) ]

dd = defaultdict(dict)
for i in range(N):
    P, A = map(int, input().split())
    dd[i][P - 1] = A

sd = SortedDict(dd)
p(sd)

for i in range(N):
    for j in range(N - 1, i -1, -1):
        if i == 0 and j == N - 1:
            continue

        # Numbers of consumed blocks.
        used_left = N - 1 - j
        used_right = i
        p("i=", i, ", j=", j, ", used left blocks=", used_left, ", used right blocks=", used_right)

        left_pointer = used_left
        right_pointer = N - 1 - used_right
        p("as matrix index from 0 to N - 1, left_pointer=", left_pointer, ", right_pointer=", right_pointer)

        right_score = left_score = 0
        # TODO : Calculate 'right_score' and 'left_score'.
        if (i != 0) and (j != N - 1):
            dp[i][j] = max(dp[i - 1][j] + right_score,
                           dp[i][j + 1] + left_score)
        elif i == 0:
            dp[i][j] = dp[i][j + 1] + left_score
        elif (j == N - 1):
            dp[i][j] = dp[i - 1][j] + right_score

    p(dp)

ans = 0
for i in range(N):
    ans = max(dp[i][i], ans)
print(ans)
