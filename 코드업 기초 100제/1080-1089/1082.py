# 1082 : [기초-종합] 16진수 구구단?

hexNum = input()

parseInt = int(hexNum, 16)

for num in range(1, 16):
    result = parseInt * num
    print("%s*%X=%X" % (hexNum, num, result))