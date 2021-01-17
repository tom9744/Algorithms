# 1068 : [기초-조건/선택실행구조] 정수 1개 입력받아 평가 출력하기

integer = int(input())

if 90 <= integer <= 100:
    print("A")
elif 70 <= integer < 90:
    print("B")
elif 40 <= integer < 70:
    print("C")
else:
    print("D")
