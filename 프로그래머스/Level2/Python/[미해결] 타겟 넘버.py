# 코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 타겟 넘버 (Level2)
answer = 0


def DFS(numbers, target, current, index):
    global answer

    if len(numbers) == index:
        if current == target:
            answer += 1
        return

    DFS(numbers, target, current + numbers[index], index + 1)
    DFS(numbers, target, current - numbers[index], index + 1)


def solution(numbers, target):
    global answer

    DFS(numbers, target, 0, 0)

    return answer
