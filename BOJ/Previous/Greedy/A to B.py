# 16953 : A → B
#
# A에서 B를 만드는 최소 횟수를 구하기위해, 주어진 방법 두 가지를 이용해 B에서 A로 돌아올 수 있는지 파악한다.
# B의 맨 뒷자리가 1이면 1을 추가한 것이고, 2로 나누어 떨어지면 2를 곱한 경우이다.
# B가 25와 같은 수라서 2로 나누어 떨어지지도, 1을 추가한 것도 아니면 만들 수 없는 것으로 판단하고 -1을 출력한다.
# A와 B가 같아지는 경우 반복문을 종료하고 결과를 출력한다.


a, b = map(int, input().split())

count = 0
is_possible = True

while b != a:
    if b == 0:
        is_possible = False
        break

    if b % 2 == 0:
        count += 1
        b = b // 2
    elif b % 10 == 1:
        count += 1
        b = b // 10
    else:
        is_possible = False
        break

if is_possible:
    print(count + 1)
else:
    print(-1)
