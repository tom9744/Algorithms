# 1084 : [기초-종합] 빛 섞어 색 만들기

R, G, B = map(int, input().split())

for valueR in range(R):
    for valueG in range(G):
        for valueB in range(B):
            print("{0} {1} {2}".format(valueR, valueG, valueB))


print(R * G * B)