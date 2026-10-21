#!/usr/bin/env python3

from collections import deque

if __name__ == "__main__":
    Q = int(input())
    d = deque([])
    for i in range(Q):
        s = input()
        if s[0] == '1':
            q, x = s.split()
            d.appendleft(x)
        elif s[0] == '2':
            print(d[len(d) - 1])
        elif s[0] == '3':
            d.pop()
