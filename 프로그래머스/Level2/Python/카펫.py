# 코딩테스트 연습 > 완전탐색 > 카펫 (Level2)
def solution(brown, yellow):
    answer = []

    total = brown + yellow  # 타일 개수의 총합
    for num in range(1, total + 1):
        # 타일 개수 총합을 나눌 수 있는 수를 찾는다.
        if total % num == 0:
            # 나눈 수가 가로 길이, 나눈 몫이 세로 길이가 된다.
            row, col = num, total // num
            # (가로 * 2) + (세로 * 2) - 4를 계산해 테두리 개수를 구하고, 그 값이 brown 값과 같은지 검토한다.
            if (row * 2) + (col * 2) - 4 == brown:
                answer = [row, col]

    return answer


print(solution(10, 2))  # [4, 3]
print(solution(8, 1))  # [3, 3]
print(solution(24, 24))  # [8, 6]
