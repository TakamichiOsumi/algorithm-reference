#!/usr/bin/env python3

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


def solve(N, sorted_data, K):
    p(sorted_data)
    val = 0

    left = 0
    while left < N:
        right = left + 1
        p("[external] left=", left, ", right=", right)
        while right <= (N - 1) and \
              (sorted_data[right][0] - sorted_data[left][0]) <= K:
            right += 1
        # Get the subset that satisfies the range whose diff is within 'K'.
        sub = sorted_data[left:right]
        p("sub=", sub)

        # Sort the subset by the other key (x[1]).
        sorted_BA = sorted(sub, reverse = False, key = lambda x : x[1])

        # Skip the unsatisfactory case.
        # 'right' might be pointing index that generates a diff > 'K'.
        if (left - right == 1) and (sorted_data[right][0] - sorted_data[left][0]) > K:
            left = left + 1
            continue

        # This subset is valid to be verified for the answer.
        internal_left = 0
        while internal_left < len(sorted_BA):
            internal_right = internal_left + 1
            ans = 0
            while internal_right <= (len(sorted_BA) - 1) and \
                  (sorted_BA[internal_right][1] - sorted_BA[internal_left][1]) <= K:
                ans += 1
                internal_right += 1
            p("[internal] left=", internal_left, ", right=", internal_right)
            # Similarly, 'internal_right' might point to index that generates
            # a diff > 'K'. Skip this iteration if this wrong condition is True.
            if not ((internal_left - internal_right == 1) and \
               (sorted_BA[internal_right][1] - sorted_BA[internal_left][1] > K)):
                val = max(val, ans + 1)
            internal_left = internal_left + 1

        left = left + 1

    p("return=", val)

    return val

if __name__ == "__main__":
    N, K = map(int, input().split())
    A_B = [ list(map(int, input().split())) for _ in range(N) ]

    if N == 1:
        print(1)
        exit()

    sAB = sorted(A_B, reverse = False, key = lambda x : x[0])
    print(solve(N, sAB, K))
