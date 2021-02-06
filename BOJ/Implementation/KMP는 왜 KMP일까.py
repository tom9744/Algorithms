# 2902 : KMP는 왜 KMP일까?

long_string = input()
parts = long_string.split("-")
result = []

for part in parts:
    result.append(part[0])

print("".join(result))