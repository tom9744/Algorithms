# 코딩테스트 연습 > 완전 탐색 > 소수 찾기 (Level2)
from itertools import permutations


def get_possible_numbers(numbers):
    possible_numbers = set()

    for n in range(1, len(numbers) + 1):
        for each in list(permutations(numbers, n)):
            possible_numbers.add(int("".join(each)))

    return possible_numbers


def solution(numbers):
    answer = 0
    numbers = sorted(list(numbers), reverse=True)
    max_number = int("".join(numbers))

    # 순열을 이용해 가능한 수 조합을 모두 구한다.
    possible_numbers = get_possible_numbers(numbers)

    # 에라토스테네스의 체로 범위 내의 소수를 구한다.
    is_prime = [False, False] + [True for _ in range(2, max_number + 1)]

    for num in range(2, int(max_number ** 0.5) + 1):
        if is_prime[num]:
            for multiplied_num in range(num + num, max_number + 1, num):
                is_prime[multiplied_num] = False

    for num in possible_numbers:
        if is_prime[num]:
            answer += 1

    return answer