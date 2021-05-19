stations = [list(map(int, input().split())) for _ in range(10)]

train = 0          # 현재 기차에 타고 있는 승객 수
max_passenger = 0  # 최대 승객 수

for hop_off, hop_on in stations:
    train -= hop_off  # 하차
    train += hop_on   # 탑승

    # 최대 승객 수를 갱신한다.
    max_passenger = max(max_passenger, train)

print(max_passenger)
