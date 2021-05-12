N = int(input())
white = [[0 for _ in range(100)] for _ in range(100)]
papers = [tuple(map(int, input().split())) for _ in range(N)]

# 색종이 영역을 검은색(1)으로 칠한다.
for left, bottom in papers:
    for x in range(10):
        for y in range(10):
            white[bottom + x][left + y] = 1

result = 0

for row in white:
    # 검은색으로 색칠된 영역의 수를 센다.
    result += row.count(1)

print(result)
