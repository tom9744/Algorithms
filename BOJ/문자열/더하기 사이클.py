current_number = input()
origin_number = int(current_number)
count = 0

while True:
    # 현재 정수의 각 자리수를 더한다.
    summary = sum(map(int, current_number))

    # 현재 정수의 마지막 자리수와 새로 만든 수의 마지막 자리수를 더해 새로운 정수를 만든다.
    current_number = current_number[-1] + str(summary)[-1]

    # 사이클 횟수를 증가시킨다.
    count += 1

    # 현재 정수가 시작 정수와 같아지면 반복문을 종료한다.
    if origin_number == int(current_number):
        break

print(count)
