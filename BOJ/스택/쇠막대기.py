brackets = input().replace("()", "L")  # 레이저 "()"는 식별하기 쉬운 문자로 바꾼다.
stack = []
steel_bars = []
result = 0

for index, bracket in enumerate(brackets):
    if bracket == "(":
        stack.append(index)
    if bracket == ")":
        start_index = stack.pop()
        steel_bars.append((start_index, index))  # 막대의 시작, 끝 인덱스를 저장한다.

# 각 막대기에 대해, 레이저에 의해 몇개의 막대로 잘리는지 계산한다.
for start, end in steel_bars:
    bar = brackets[start:end + 1]
    result += bar.count("L") + 1   # 잘린 막대 수 = 범위 내 레이저 개수 + 1

print(result)
