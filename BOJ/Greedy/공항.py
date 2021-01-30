# 10775 : 공항
#
# 시간초과....ㅠ

G = int(input())
P = int(input())
gates = [0 for _ in range(G)]

for i in range(P):
    gi = int(input())
    target_gates = gates[0:gi]

    if sum(target_gates) == gi:
        break
    else:
        for position in range(gi):
            if gates[gi - position - 1] == 0:
                gates[gi - position - 1] = 1
                break

print(sum(gates))
