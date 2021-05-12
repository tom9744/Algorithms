# 3009 : 네 번째 점
import sys

X = []
Y = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    if X.count(x) > 0:
        X.remove(x)
    else:
        X.append(x)

    if Y.count(y) > 0:
        Y.remove(y)
    else:
        Y.append(y)

print(f"{X.pop()} {Y.pop()}")