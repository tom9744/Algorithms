# 1066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기

def isEven(num):
    if num % 2 is 0:
        return "even"
    else:
        return "odd"


integerA, integerB, integerC = map(int, input().split())

evenIntegers = map(isEven, [integerA, integerB, integerC])

for integer in evenIntegers:
    print(integer)


