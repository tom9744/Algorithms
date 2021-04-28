N = int(input())
commands = [input() for _ in range(N)]
length = len(commands[0])
result = []

# 모든 문자열에 대해, 같은 위치에 같은 글자만 존재하는지 확인한다.
# index  :  0   1   2   3   4   5   6   7   8   9
# cmdA   : [c] [o] [n] [f] [i] [g] [.] [s] [y] [s]
# cmdB   : [c] [o] [n] [f] [i] [g] [.] [i] [n] [f]
# cmdC   : [c] [o] [n] [f] [i] [g] [u] [r] [e] [s]
# result :  c   o   n   f   i   g   ?   ?   ?   ?
for position in range(length):
    is_different = False
    first_command = commands[0]

    # 다른 문자가 발견되면 플래그를 참으로 변경하고, 반복문을 종료한다.
    for command in commands:
        if command[position] != first_command[position]:
            is_different = True
            break

    result.append("?" if is_different else first_command[position])

print("".join(result))
