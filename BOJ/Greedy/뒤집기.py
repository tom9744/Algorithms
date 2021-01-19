# 1439 : 뒤집기
#
# 시작 숫자가 아닌 수로 변하는 위치의 개수를 세면 된다.
# 예를 들어, 0으로 시작된 경우, 0에서 1로 변하는 위치의 개수를 센다.
# (ex) 00[01]1100[01]11000 => 2
#


sequence = input()

start = sequence[0]
count = 0

for index in range(1, len(sequence)):
    if sequence[index] is not start and sequence[index] is not sequence[index - 1]:
        count += 1

print(count)