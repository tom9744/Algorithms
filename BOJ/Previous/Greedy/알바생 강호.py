# 1758 : 알바생 강호
#
# 금액이 큰 손님부터 먼저 커피를 제공하면 된다.
# 따라서 배열을 내림차순 정렬한 뒤, 팁을 계산하는 연산을 수행한다.

N = int(input())
tips_in_mind = []

for _ in range(N):
    tips_in_mind.append(int(input()))

tips_in_mind.sort(reverse=True)

tips_given = []
rank = 1

for tip in tips_in_mind:
    calculated = tip - (rank - 1)

    tips_given.append(calculated if calculated > 0 else 0)
    rank += 1

print(sum(tips_given))