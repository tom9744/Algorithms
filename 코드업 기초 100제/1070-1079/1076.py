# 1076 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기

char = input()
number = ord(char)

current_number = ord('a')

while current_number <= number:
    print(chr(current_number), end=' ')
    current_number += 1

