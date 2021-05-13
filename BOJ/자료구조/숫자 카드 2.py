import collections

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

# 빈도수 해시맵을 생성한다.
frequency = collections.Counter(cards)  # O(N)
result = []

# 빈도수 해시맵을 조회하여 카드의 개수를 찾는다.
for target in targets:
    result.append(str(frequency[target]))  # O(1)

print(" ".join(result))