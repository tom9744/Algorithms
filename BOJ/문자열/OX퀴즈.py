T = int(input())

for _ in range(T):
    seq = input()

    result = 0
    score = 0

    for ans in seq:
        # 정답인 경우, 점수를 증가시켜 나간다.
        if ans == 'O':
            score += 1
        # 오답을 만나면 점수를 초기화한다.
        else:
            score = 0

        # 현재 점수를 누적한다.
        result += score

    print(result)
