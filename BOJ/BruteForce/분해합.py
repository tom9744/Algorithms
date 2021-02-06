# 2231 : 분해합
#
# 주어진 숫자 N 부터 0 까지 순회하면서 문제에 주어진 조건에 따라 숫자를 생성해 본다.
# 생성 결과와 주어진 숫자 N 이 동일하면, 후보군 배열에 추가한다.
#
# 마지막으로 반복문이 종료되면, 후보군 배열에서 가장 작은 값을 찾아 출력한다.

N = int(input())
candidates = []

for number in range(N, 0, -1):
    digits = list(map(int, str(number)))
    generated = number

    for digit in digits:
        generated += digit

    if generated == N:
        candidates.append(number)

if len(candidates) == 0:
    print(0)
else:
    print(min(candidates))