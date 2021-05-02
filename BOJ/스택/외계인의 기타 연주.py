from sys import stdin

N, P = map(int, stdin.readline().rstrip().split(" "))

guitar = {
    "1": [], "2": [],
    "3": [], "4": [],
    "5": [], "6": [],
}

count = 0

for _ in range(N):
    line, fret = stdin.readline().rstrip().split(" ")
    fret = int(fret)

    # 주어진 줄의 더 높은 프렛을 누르고 있는 경우, 손가락을 하나씩 뗀다.
    while guitar[line] and guitar[line][-1] > fret:
        guitar[line].pop()
        count += 1

    # 같은 줄, 같은 프렛인 경우 스킵한다.
    if guitar[line] and guitar[line][-1] == fret:
        continue

    # 주어진 프렛을 현재 줄(= 스택)에 삽입한다.
    guitar[line].append(fret)
    count += 1

print(count)