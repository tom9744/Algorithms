# 2163 : 초콜릿 자르기

N, M = map(int, input().split())

short = min(N, M)
long = max(N, M)

result = (short - 1) + (long - 1) * short

print(result)