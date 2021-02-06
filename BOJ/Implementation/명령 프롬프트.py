# 1032 : 명령 프롬프트
#
# 가장 먼저 입력으로 들어오는 문자열을 별도로 저장하고, 문자열의 길이를 파악해 같은 길이의 0으로 초기화 된 배열을 선언한다.
# 다음부터 들어오는 문자열을 첫 번째 문자열과 비교하면서, 글자가 다른 부분에 해당하는 배열 값을 +1 한다.
#
# 배열 값이 0인 부분은 위치에 해당하는 글자를, 그렇지 않은 부분은 ?를 출력하도록 하면 정답이다.

import sys

N = int(sys.stdin.readline().rstrip())

first = list(sys.stdin.readline().rstrip())
length = len(first)

differences = [0 for _ in range(length)]

for _ in range(1, N):
    file_name = list(sys.stdin.readline().rstrip())

    for idx in range(len(file_name)):
        if first[idx] != file_name[idx]:
            differences[idx] += 1

result = []
for idx in range(len(differences)):
    if differences[idx] != 0:
        result.append("?")
    else:
        result.append(first[idx])

print("".join(result))