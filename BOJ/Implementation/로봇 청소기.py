# 14503 : 로롯 청소기

def rotate(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    elif d == 3:
        return 2


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = []

for _ in range(N):
    room.append(list(map(int, input().split())))

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
rotation = 0
cleaned = 0

while True:

    if room[r][c] == 0:
        room[r][c] = 2
        cleaned += 1

    left = rotate(d)
    next_r = r + dr[left]
    next_c = c + dc[left]
    if (0 <= next_r < N and 0 <= next_c < M) and room[next_r][next_c] == 0:
        rotation = 0
        d = left
        r = next_r
        c = next_c
    else:
        rotation += 1
        d = left

    if rotation == 4:
        rotation = 0

        if d == 0:
            r += 1
        elif d == 1:
            c -= 1
        elif d == 2:
            r -= 1
        elif d == 3:
            c += 1

        if room[r][c] == 1:
            break

print(cleaned)



