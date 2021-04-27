expression = input()
plus_chunks = expression.split("-")
result = 0

# 첫번째 값을 제외한 모든 Chunk 값을 빼면 최소값을 구할 수 있다.
# 50-40+30-20 -> ['50' '40+30', '20'] -> 50 - 70 - 20 = -40
# 50+40-30+20 -> ['50+40', '30+20'] -> 90 - 50 = 50
# 50-40-30-20 -> ['50', '40', '30', '20'] -> 50 - 40 - 30 - 20 = -40
for idx, chunk in enumerate(plus_chunks):
    value = sum(map(int, chunk.split("+")))

    if idx == 0:
        result += value
    else:
        result -= value

print(result)

