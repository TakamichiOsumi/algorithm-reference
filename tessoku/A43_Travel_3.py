#!/usr/bin/env python3

if __name__ == "__main__":
    N, L = map(int, input().split())

    ans = []
    for i in range(N):
        distance, direction = input().split()
        distance = int(distance)
        if direction == 'E':
            ans.append(abs(L - distance))
        else:
            # 'W'
            ans.append(distance)

    print(max(ans))
