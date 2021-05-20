N = int(input())
numbers = list(map(int, input().split()))
combinations = []


def get_three_numbers(index=0):
    if len(combinations) == 3:
        ai, aj, ak = combinations

        if aj - ai == ak - aj:
            return 1  # 등차수열인 경우, 1 반환
        else:
            return 0

    count = 0

    for idx in range(index, N):
        combinations.append(numbers[idx])
        count += get_three_numbers(idx + 1)  # 길이 3짜리 등차수열의 개수를 센다.
        combinations.pop()

    return count


print(get_three_numbers())
