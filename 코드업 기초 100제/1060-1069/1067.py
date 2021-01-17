# 1067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분석하기

integer = int(input())

if integer < 0:
    print("minus")
else:
    print("plus")

if integer % 2 is 0:
    print("even")
else:
    print("odd")