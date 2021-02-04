# 2108 : 통계학
#
# 얼핏 쉬워 보이는 문제인데, 시간초과 문제 때문에 고생했다.
# 최빈값을 반복문을 이용해 풀었지만, 'Collections'의 'Counter()', 'most_common()' 함수를 사용하면
# 더 쉽게 풀이할 수 있을 것 같다. (참고로 아래 코드는 Pypy3 에서만 가능. Python3 시간초과)


def get_average(numbers, length):
    return round(sum(numbers) / length)


def get_middle(numbers, length):
    return numbers[length // 2]


def get_most_frequent(numbers, length):
    frequency = []

    count = 1
    for idx in range(length - 1):
        if numbers[idx] == numbers[idx + 1]:
            count += 1
        else:
            frequency.append((count, numbers[idx]))
            count = 1

    frequency.append((count, numbers[length - 1]))

    frequency.sort(key=lambda elem: elem[1])
    frequency.sort(key=lambda elem: elem[0], reverse=True)

    if len(frequency) == 1:
        return frequency[0][1]
    else:
        if frequency[0][0] == frequency[1][0]:
            return frequency[1][1]
        else:
            return frequency[0][1]


def get_min_max_difference(numbers, length):
    return numbers[length - 1] - numbers[0]


N = int(input())
integers = []
for _ in range(N):
    integers.append(int(input()))

integers.sort()

print(get_average(integers, N))
print(get_middle(integers, N))
print(get_most_frequent(integers, N))
print(get_min_max_difference(integers, N))
