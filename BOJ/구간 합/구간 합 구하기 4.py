import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 누적 합
accumulate = [0, ]
acc = 0
for idx in range(N):
    acc += numbers[idx]
    accumulate.append(acc)

for _ in range(M):
    i, j = map(int, input().split())

    # 구간 합 공식(Result = P[R] - P[L-1])에 따라 결과를 반환한다.
    print(accumulate[j] - accumulate[i - 1])
