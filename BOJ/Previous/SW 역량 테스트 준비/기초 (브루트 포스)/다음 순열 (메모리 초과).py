from itertools import permutations

N = int(input())
numbers = tuple(map(int, input().split()))
permutation = sorted(list(permutations(numbers, N)))

for index in range(len(permutation)):
    if numbers == permutation[index]:
        if index == len(permutation) - 1:
            print(-1)
        else:
            result = ""
            for each in permutation[index + 1]:
                result += str(each) + " "

            print(result.strip())
        break

# 메모리 초과!
