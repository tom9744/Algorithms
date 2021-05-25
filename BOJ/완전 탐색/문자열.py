A, B = input().split()

min_difference = float("inf")

for i in range(len(B) - len(A) + 1):
    difference = 0
    # 문자열 A와 문자열 B의 부분 문자열의 차이를 계산한다.
    for j, char in enumerate(A):
        if char != B[i + j]:
            difference += 1

    min_difference = min(min_difference, difference)

print(min_difference)
