# 1157 : 단어 공부
#
# 문자를 글자 단위로 쪼개서 배열로 만들고, 오름/내림차순 상관없이 일단 정렬한다.
# 배열 원소를 하나씩 체크하면서 count 를 증가시키고, 원소가 바뀌는 경우 해당 원소와 누적된 count 값을 저장한다.
# 이렇게 누적된 값들이 들어있는 배열을 count 기준으로 내림차순 정렬하고, 맨 앞 두개를 꺼내서 비교해본다.
# 맨 앞 두개의 count 가 같으면 "?"를, 그렇지 않다면 가장 첫번째 것에 들어있는 원소를 대문자로 바꿔서 출력한다.
# 다만, 단어의 길이가 1인 경우 그대로 대문자로 바꿔서 출력한다.

import sys

word = list(sys.stdin.readline().rstrip().lower())

if len(word) == 1:
    print(word.pop().upper())
else:
    word.sort()

    used = []
    prev = word.pop(0)
    count = 1

    for char in word:

        if char != prev:
            used.append([prev, count])
            prev = char
            count = 1
        else:
            count += 1

    used.append([prev, count])

    used.sort(key=lambda elem: elem[1], reverse=True)

    first = used.pop(0)
    second = used.pop(0)

    if first[1] == second[1]:
        print("?")
    else:
        print(first[0].upper())
