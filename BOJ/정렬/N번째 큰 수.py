T = int(input())

for _ in range(T):
    array = list(map(int, input().split()))
    print(sorted(array, reverse=True)[2])
