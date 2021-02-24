# 10844 : 쉬운 계단 수
#
# 처음에 점화식을 구하기 위해 N = 5인 경우까지 직접 구해보니, 맨 끝자리 수가 0, 9인 경우와 그렇지 않은 경우로 나누어졌다.
# 따라서, 1~9까지 숫자를 배열로 표현해 가능한 계단 수를 모두 구해 배열에 추가하는 방법으로 접근했으나 메모리 초과가 났다.
#
# 검색 결과 비슷하지만 DP의 개념을 적극 사용한 접근법이 있었고, 구현해보니 정답처리 받을 수 있었다.
# DP 개념을 아직 100% 이해하지 못한 것 같다.

N = int(input())
DP = [[1 for _ in range(10)] for _ in range(N)]

for iteration in range(1, N):
    for number in range(10):
        if number == 0:
            DP[iteration][number] = DP[iteration - 1][number + 1]
        elif number == 9:
            DP[iteration][number] = DP[iteration - 1][number - 1]
        else:
            DP[iteration][number] = DP[iteration - 1][number + 1] + DP[iteration - 1][number - 1]

result = sum(DP[N - 1]) - DP[N - 1][0]
print(result % 1000000000)

# 메모리 초과
# N = int(input())
# DP = [[num + 1] for num in range(9)]
#
# for _ in range(N - 1):
#     for number in range(9):
#         extended = []
#         for each in DP[number]:
#             last_digit = each % 10
#             case_1 = (each * 10) + (last_digit - 1)
#             case_2 = (each * 10) + (last_digit + 1)
#
#             if last_digit == 0:
#                 extended.append(case_2)
#             elif last_digit == 9:
#                 extended.append(case_1)
#             else:
#                 extended.append(case_1)
#                 extended.append(case_2)
#
#         DP[number] = extended
#
# result = 0
#
# for each in DP:
#     result += len(each)
#
# print(result % 1000000000)
