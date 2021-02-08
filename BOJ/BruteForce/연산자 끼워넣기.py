# 14888 : 연산자 끼워넣기
#
# 단순히 permutations 만 사용하여 풀이한 경우, 시간초과가 나왔다.
# 따라서 permutations 결과에 set 을 적용하여 중복되는 순열이 존재하지 않도록 해주어야 한다.
#
# 추가적으로 모든 결과를 담은 배열을 오름차순 정렬하려 맨 앞/맨 뒤 원소를 가져오지 않고
# 매 계산마다 최소 최대를 비교하여 값을 갱신해준다.

from itertools import permutations

N = int(input())
integers = list(map(int, input().split()))
operator_count = list(map(int, input().split()))
operators = []
for index in range(4):
    if index == 0:
        for _ in range(operator_count[index]):
            operators.append(0)
    if index == 1:
        for _ in range(operator_count[index]):
            operators.append(1)
    if index == 2:
        for _ in range(operator_count[index]):
            operators.append(2)
    if index == 3:
        for _ in range(operator_count[index]):
            operators.append(3)

minimum = 1000000001
maximum = -1000000001

for each in list(set(permutations(operators, N - 1))):
    result = integers[0]
    for index in range(N - 1):
        if each[index] == 0:
            result = result + integers[index + 1]
        elif each[index] == 1:
            result = result - integers[index + 1]
        elif each[index] == 2:
            result = result * integers[index + 1]
        elif each[index] == 3:
            if result > 0:
                result = result // integers[index + 1]
            else:
                result = -(abs(result) // integers[index + 1])

    if result < minimum:
        minimum = result
    if result > maximum:
        maximum = result

print(maximum)
print(minimum)