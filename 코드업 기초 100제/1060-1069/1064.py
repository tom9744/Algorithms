# 1064 : [기초-삼항연산] 정수 3개 입력받아 가장 작은 수 출력하기

integerA, integerB, integerC = map(int, input().split())

print(integerA if (integerA < integerB) and (integerA < integerC) else integerB if integerB < integerC else integerC)
