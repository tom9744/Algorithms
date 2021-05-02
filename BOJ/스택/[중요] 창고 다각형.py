from sys import maxsize
from collections import defaultdict


# 변곡점이 나올때 까지 현재의 최대값으로 배열을 채워 반환한다.
def scan(array, start_idx, end_idx, reverse=False):
    current = 0
    result = []

    for idx in range(start_idx, end_idx, -1 if reverse else 1):
        current = max(current, array[idx])
        result.append(current)

    return result


N = int(input())
start, end = maxsize, -maxsize
columns = defaultdict(int)

for _ in range(N):
    position, height = map(int, input().split(" "))
    start = min(start, position)
    end = max(end, position)
    columns[position] = height

# 왼쪽과 오른쪽에서 보았을 때, 눈에 보이는 막대 높이만 저장한다.
# (ex) left : [ 4,  4,  6,  6,  6,  6, 10, 10, 10, 10, 10, 10, 10, 10]
# (ex) right: [10, 10, 10, 10, 10, 10, 10,  8,  8,  8,  8,  8,  8,  8]
left = scan(columns, start, end + 1)
right = reversed(scan(columns, end, start - 1, True))
volume = 0

# 이후 왼쪽, 오른쪽에서 눈에 보이는 막대 높이 중 최소 값을 선택하면 된다.
# (ex): [4, 4, 6, 6, 6, 6, 10, 8, 8, 8, 8, 8, 8, 8]
for left, right in zip(left, right):
    volume += min(left, right)

print(volume)
