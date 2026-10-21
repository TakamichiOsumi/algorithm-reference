#!/usr/bin/env python3

# The main logic is to allocate scores to each color
# and analyze conversion scores after the color changes.
#
# When W == 0, R == 1, B == 2, all conversion
# affects score reduction of 0 or -3, which means
# no score change like WW => W or point - 3 like RB => W.
#
# Thus, count up the initial score of A, divide it by 3
# and check the remainder with C, as below.

if __name__ == "__main__":
    N, C = input().split()
    N = int(N)
    A = list(input())

    score = 0
    for a in A:
        if a == 'W':
            score += 0
        elif a == 'R':
            score += 1
        elif a == 'B':
            score += 2

    folded = score % 3
    if (folded == 0 and C == 'W') or \
       (folded == 1 and C == 'R') or \
       (folded == 2 and C == 'B'):
        print("Yes")
    else:
        print("No")
