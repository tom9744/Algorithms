# 2953 : 나는 요리사다

scores = []
max = 0

for _ in range(5):
    score = sum(map(int, input().split()))
    scores.append(score)

    if max < score:
        max = score

print(scores.index(max) + 1)
print(max)
