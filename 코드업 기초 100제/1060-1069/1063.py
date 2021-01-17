# 1063 : [기초-삼항연산] 두 정수 입력받아 큰 수 출력하기

integerA, integerB = map(int, input().split())

print(integerA if integerA > integerB else integerB)