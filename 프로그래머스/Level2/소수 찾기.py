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


# 더 이상 플래그가 없을 때 까지 반복하며, 플래그 검증 수행
while flags:
    flag_name = flags.pop(0)

    # flag_name이 '-'로 시작하는 경우 추가 검증 수행
    if flag_name.startswith("-"):
        # 해당 flag_arg_type에 해당하는 규칙을 딕셔너리에서 탐색
        flag_arg_type = parsed_rule[flag_name]

        if flag_arg_type == "NULL":
            continue  # NULL인 경우, 다음 반복에서 "-"로 시작하지 않는 flag 값이 들어오면
        else:
            flag_arg = flags.pop(0)

            if flag_arg_type == "STRING" and re.findall("[^a-zA-Z]+", flag_arg):
                is_valid = False
            elif flag_arg_type == "NUMBER" and re.findall("[^0-9]+", flag_arg):
                is_valid = False
    # flag_name이 '-'로 시작하지 않는 경우, 검증 성공 플래그를 False로 변경 후 즉시 반복문 종료
    else:
        is_valid = False
        break

answer.append(is_valid)