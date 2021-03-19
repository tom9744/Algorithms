# 코딩테스트 연습 > 정렬 > 가장 큰 수 (Level2)
def solution(numbers):
    numbers = list(map(str, numbers))
    # 숫자의 값이 1000 이하이므로 3자리 수로 맞춘 뒤 비교한다. (666, 101010, 222)
    numbers.sort(key=lambda elem: elem * 3, reverse=True)

    # 모든 값이 0인 경우, 즉 000인 경우 0으로 만들어준다.
    return str(int(''.join(numbers)))


print(solution([6, 10, 2]))  # 6210
print(solution([3, 30, 34, 5, 9]))  # 9534330

