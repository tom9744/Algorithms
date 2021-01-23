# 1946 : 신입사원
#
# 두 전형의 점수 중 하나로 오름차순 정렬한 뒤,
# 나머지 전형의 점수로 탈락 여부를 결정한다.

num_of_test_cases = int(input())

for _ in range(num_of_test_cases):
    num_of_candidates = int(input())
    ranks = []

    for _ in range(num_of_candidates):
        ranks.append(tuple(map(int, input().split())))

    ranks.sort()

    count = 1
    highest_rank = ranks[0][1]

    for index in range(1, len(ranks)):
        if ranks[index][1] < highest_rank:
            highest_rank = ranks[index][1]
            count += 1

    print(count)