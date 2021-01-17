# 1087 : [기초-종합] 여기까지! 이제 그만~

targetNum = int(input())
num = 1
acc = 0

while acc < targetNum:
    acc += num
    num += 1

print(acc)

