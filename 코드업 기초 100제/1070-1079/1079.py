# 1079 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기

chars = input().split()

for char in chars:

    print(char)

    if char is 'q':
        break
