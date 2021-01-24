# 18238 : ZOAC 2
#
# 알파벳 배열을 선언하고, 입력으로 들어온 문자열을 구성하는 글자 하나씩 배열에서의 위치(인덱스)를 구한다.
# 현재 글자의 인덱스와 다음 글자의 인덱스를 비교해, 오른쪽 / 왼쪽으로 이동할 경우 필요한 이동횟수를 구한다.
# 이후, 오른쪽 / 왼쪽으로 이동하는 경우 중 이동횟수가 작은 쪽으로 이동하도록 하고 카운트에 누적한다.

alphabets = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

string = input()
current_position = 0
count = 0

for char in string:
    next_position = alphabets.index(char)

    if current_position <= next_position:
        right = next_position - current_position
        left = 26 - right
    else:
        right = 26 - abs(next_position - current_position)
        left = 26 - right

    count += left if left <= right else right

    current_position = next_position

print(count)
