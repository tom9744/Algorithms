# 14659 : 한조 서열 정리하고옴
#
# 임시 변수에 시작 봉우리 높이를 저장하고 왼쪽 봉우리에서 오른쪽으로 이동한다.
# 다음 봉우리의 높이가 낮으면 카운터를 증가시키고, 그렇지 않으면 카운터를 초기화하고 다음 봉우리부터 새로 시작한다.
# 이때, 현재 카운터가 역대 최대값보다 크다면 최대값을 갱신한다.

num_of_peaks = int(input())
peak_heights = list(map(int, input().split()))

maximum_kill = 0
current_kill = 0
current_height = peak_heights[0]

for index in range(1, len(peak_heights)):

    if current_height > peak_heights[index]:
        current_kill += 1
        if maximum_kill < current_kill:
            maximum_kill = current_kill
    else:
        current_kill = 0
        current_height = peak_heights[index]

print(maximum_kill)