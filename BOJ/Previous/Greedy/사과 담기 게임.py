# 2828 : 사과 담기 게임
#
# 바구니의 양 끝(왼쪽, 오른쪽) 위치를 파악하고, 떨어지는 사과의 위치와 비교한다.
# 사과가 바구니 범위 내에서 떨어지면 움직이지 않고, 오른쪽 끝보다 큰 값의 위치에서 떨어지면 (사과 위치 - 바구니 오른쪽 끝)만큼 이동한다.
# 마찬가지로 왼쪽 끝보다 작은 값의 위치에서 떨어지면 (바구니 왼쪽 끝 - 사과 위치)만큼 이동한다.

n, m = map(int, input().split())
apples = int(input())

drop_point = []
for _ in range(apples):
    drop_point.append(int(input()))

start, end = 1, m
move = 0

for point in drop_point:
    if start <= point <= end:
        continue
    elif point > end:
        distance = abs(point - end)
        move += distance
        start += distance
        end += distance
    elif point < start:
        distance = abs(point - start)
        move += distance
        start -= distance
        end -= distance

print(move)


