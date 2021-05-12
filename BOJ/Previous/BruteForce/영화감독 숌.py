# 1436 : 영화감독 숌
#
# 숫자를 666부터 증가시키면서 '666'이 포함된 경우 count 를 증가시킨다.
# count 값이 N과 동일해지면 반복문을 종료하고 가장 마지막에 나타난 '666'을 포함하는 숫자를 반환한다.

N = int(input())
count = 0
number = 666
result = 0

while count != N:

    if str(number).find("666") != -1:
        result = number
        count +=1

    number += 1

print(result)