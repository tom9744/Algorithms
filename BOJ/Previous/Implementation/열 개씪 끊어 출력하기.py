import sys

N = list(sys.stdin.readline().rstrip())
temp = []

for idx in range(len(N)):
    if idx != 0 and idx % 10 == 0:
        print("".join(temp))
        temp = []

    temp.append(N[idx])

if len(temp) > 0:
    print("".join(temp))
