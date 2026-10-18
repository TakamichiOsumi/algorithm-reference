#!/usr/bin/env python3

N, M, B = map(int, input().split())

A = list(map(int, input().split()))
C = list(map(int, input().split()))

total_A = sum(A)
total_C = sum(C)

ans = 0
for a in A:
    ans += ((len(C) * a) + total_C)

ans = ans + (len(A) * len(C) * B)
print(ans)
