import sys

word = list(sys.stdin.readline().rstrip())
result = []

base = 97
for idx in range(26):
    alphabet = chr(base + idx)

    try:
        first_appear = word.index(alphabet)

        result.append(first_appear)
    except ValueError as error:
        result.append(-1)

for each in result:
    print(each, end=" ")