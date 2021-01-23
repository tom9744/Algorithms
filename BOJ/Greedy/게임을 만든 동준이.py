# 2847 : 게임을 만든 동준이
#
# 가장 마지막에 있는 레벨의 점수가 가장 높아야 하므로, 배열의 맨 뒤 요소의 값을 최대값으로 설정한다.
# 이후 배열의 앞으로 이동하면서 현재의 최대값보다 큰 점수가 발견되면 현재 최대값보다 작아질 때까지 1씩 감소시킨다.
# 예를 들어, [5, 3, 7, 5]에서 5를 최대값으로 두고 7이 5보다 작아질 때까지 1씩 감소시킨다.
#
# 현재 최대값보다 작아지도록 만들었다면, 이제 그 수를 최대값으로 설정하고 위의 과정을 반복한다.


num_of_levels = int(input())
scores = []

for _ in range(num_of_levels):
    scores.append(int(input()))

max_score = scores[len(scores) - 1]
count = 0

for index in range(1, len(scores)):

    current = scores[len(scores) - index - 1]

    while current >= max_score:
        count += 1
        current -= 1

    max_score = current

print(count)
