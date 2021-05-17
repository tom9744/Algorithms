N, M = map(int, input().split())
frame = [list(input()) for _ in range(N)]


def dfs(x, y):
    if x < 0 or x > N - 1 or\
            y < 0 or y > M - 1:
        return

    if frame[x][y] == "0":
        frame[x][y] = "1"
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)


count = 0

for i in range(N):
    for j in range(M):
        if frame[i][j] == "0":
            dfs(i, j)
            count += 1

print(count)

# 4 5
# 00110
# 00011
# 11111
# 00000
# result: 3

# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
# result: 8
