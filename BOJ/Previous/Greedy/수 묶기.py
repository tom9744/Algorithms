# 1744 : 수 묶기
#
# 처음 수를 입력 받을 때, 음수와 양수를 구분하여 각각 다른 배열에 삽입한다.
# 다만, 1은 어느 수에도 곱하지 않는 것이 유리하므로 바로 결과에 1을 더한다. (ex. 1 * 2 = 2, 1 + 2 = 3)
# 각각 배열을 큰 수가 앞에 오도록 정렬하고, 두개씩 뽑아 곱한 값을 결과에 더한다.
# 마지막 하나가 남는 경우, 그대로 결과에 더한다.

length = int(input())
neg, pos = [], []
acc = 0

for _ in range(length):
    num = int(input())
    if num <= 0:
        neg.append(num)
    elif num > 1:
        pos.append(num)
    else:
        acc += num

neg.sort()
pos.sort(reverse=True)
idx = 0
while len(neg) > 1:
    numA = neg[idx]
    numB = neg[idx + 1]

    acc += numA * numB
    neg.remove(numA)
    neg.remove(numB)

if len(neg) > 0:
    acc += neg.pop()

while len(pos) > 1:
    numA = pos[idx]
    numB = pos[idx + 1]

    acc += numA * numB
    pos.remove(numA)
    pos.remove(numB)

if len(pos) > 0:
    acc += pos.pop()

print(acc)