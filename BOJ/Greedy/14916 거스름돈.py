# 14916 : 거스름돈
#
# 무조건 큰 수로 나누는 방법으로 접근하면 총 금액이 13원인 경우, 5원 2개 2원 1개를 사용해 거슬러줄 수 없게된다.
# 따라서 총액에서 2를 반복해서 빼면서 동전 개수에 +1하고, 5의 배수가 되었을 때 5로 나눈 몫을 더해주면된다.
# 총액이 1이 되는 경우, 더 이상 나눌 수 없어 거스를 수 없으므로 -1을 출력한다.

money = int(input())
coins = 0

while money != 0:
    if money % 5 == 0:
        coins += money // 5
        print(coins)
        break
    if money == 1:
        print(-1)
        break

    coins += 1
    money -= 2
