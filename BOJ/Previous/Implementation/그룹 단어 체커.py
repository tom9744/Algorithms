# 1316 : 그룹 단어 체커
#
# 단어를 구성하는 글자로 이루어진 배울의 원소를 처음부터 끝까지 하나씩 체크해본다.
# 이전 글자와 현재 글자가 같은 경우 count 를 증가 시킨다.
# 이전 글자와 현재 글자가 다르면, 현재까지 누적한 이전 글자에 대한 count 값과 단어에 존재하는 이전 글자의 총 개수를 비교한다.
# 현재까지 누적한 이전 글자에 대한 count 값과 단어에 존재하는 이전 글자의 총 개수가 같지 않으면 그룹 단어가 아니므로, False 를 반환한다.
# is_group_word 함수를 실행한 결과가 True 인 경우에만 result 를 증가시킨다.

import sys


def is_group_word(string):
    chars = list(string)

    prev = chars[0]
    count = 0

    for char in chars:
        if char == prev:
            count += 1
        else:
            if count != chars.count(prev):
                return False
            count = 1

        prev = char

    return True


N = int(sys.stdin.readline().rstrip())
result = 0

for _ in range(N):
    word = sys.stdin.readline().rstrip()

    if is_group_word(word):
        result += 1

print(result)

