# 14500 : 테트로미노
#
# 테트로미노를 회전/대칭하여 만들 수 있는 모든 경우의 수에 대해 dx, dy를 구한다.
# 매번 for 문을 사용하지 않고 이렇게 접근하면, 인덱스로 배열에 접근하기만 하면 되서 시간이 단축된다.
#
# N, M 크기의 종이의 모든 위치에 대해 반복문을 수행하면서
# 위에서 구한 19개의 테트로미노를 놓는 경우의 수 중 가능한 것 (= 종이를 벗어나지 않는 것)에 대해
# 테트로미노로 덮어지는 영역에 적힌 수의 합을 구한 뒤, 누적 최대값과 비교해본다.
#
# 이렇게 반복문을 종료한 뒤, 마지막까지 누적된 최대값을 출력하면 정답이다.

tetrominos = [
    [ [0, 0, 0, 0], [0, 1, 2, 3] ],
    [ [0, 1, 2, 3], [0, 0, 0, 0] ],

    [ [0, 1, 0, 1], [0, 0, 1, 1] ],

    [ [0, 1, 2, 2], [0, 0, 0, 1] ],
    [ [0, 1, 2, 2], [0, 0, 0, -1] ],
    [ [0, 0, 1, 2], [1, 0, 0, 0] ],
    [ [0, 0, 1, 2], [-1, 0, 0, 0] ],
    [ [0, 0, 0, 1], [0, 1, 2, 2] ],
    [ [0, 0, 0, -1], [0, 1, 2, 2] ],
    [ [1, 0, 0, 0], [0, 0, 1, 2] ],
    [ [-1, 0, 0, 0], [0, 0, 1, 2] ],

    [ [0, 0, 1, 1], [0, 1, 1, 2] ],
    [ [0, 0, -1, -1], [0, 1, 1, 2] ],
    [ [0, 1, 1, 2], [0, 0, -1, -1] ],
    [ [0, 1, 1, 2], [0, 0, 1, 1] ],

    [ [0, 1, 1, 2], [0, 0, 1, 0] ],
    [ [0, 1, 1, 2], [0, 0, -1, 0] ],
    [ [0, 0, 1, 0], [0, 1, 1, 2] ],
    [ [0, 0, -1, 0], [0, 1, 1, 2] ],
]

N, M = map(int, input().split())
paper = []
max_sum = 0

for _ in range(N):
    paper.append(list(map(int, input().split())))

for x in range(N):
    for y in range(M):

        for index in range(19):
            is_valid = True
            summary = 0

            dx, dy = tetrominos[index]

            for coord in range(4):
                nx = x + dx[coord]
                ny = y + dy[coord]

                if 0 <= nx < N and 0 <= ny < M:
                    summary += paper[nx][ny]
                else:
                    is_valid = False

            if is_valid and max_sum < summary:
                max_sum = summary

print(max_sum)
