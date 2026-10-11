#!/usr/bin/env python3

N = int(input())
val = 0
for i in range(N):
    T, A = input().split()
    if T == "+":
        val += int(A)
    elif T == "*":
        val *= int(A)
    elif T == "-":
        val -= int(A)
    val %= 10000
    print(val)
    

