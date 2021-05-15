from sys import stdin

N = int(stdin.readline().rstrip())
budgets = list(map(int, stdin.readline().rstrip().split()))
total = int(stdin.readline().rstrip())

start, end = 1, max(budgets)

while start <= end:
    # 상한액 최소값과 최대값의 중간값을 구한다.
    mid = (start + end) // 2

    assigned = 0
    # 상한액 초과 여부에 따라 알맞는 금액을 배정한다.
    for budget in budgets:
        if mid < budget:
            assigned += mid
        else:
            assigned += budget

    # 최종적으로 배정된 금액과 총 예산을 비교해 상한액 범위를 조절한다.
    if assigned > total:
        end = mid - 1
    else:
        start = mid + 1

# 마지막에 산출된 상한액 범위의 마지막 값이 정답이다.
print(end)
