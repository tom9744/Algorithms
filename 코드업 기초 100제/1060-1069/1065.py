# 1065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기

def isEven(integer):
    return integer % 2 is 0


integerA, integerB, integerC = map(int, input().split())

evenIntegers = list(filter(isEven, [integerA, integerB, integerC]))

for integer in evenIntegers:
    print(integer)
