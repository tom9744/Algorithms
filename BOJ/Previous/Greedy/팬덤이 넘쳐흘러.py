num_of_fans = int(input())
durations = []
shortest = []

for _ in range(num_of_fans):
    start, end = map(int, input().split())
    durations.append((start, end))

came = sorted(durations, key=lambda elem: elem[0])  # 등교
left = sorted(durations, key=lambda elem: elem[1])  # 하교

# 등교 제일 늦게한 학생의 등교시간 - 하교 제일 먼저한 학생의 하교시간
result = came[-1][0] - left[0][1]

print(result if result > 0 else 0)