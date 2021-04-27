from collections import Counter

A = int(input())
B = int(input())
C = int(input())

# 각 자리수를 문자로 변환하고 Counter 라이브러리를 이용해 빈도수를 계산한다.
result = Counter(list(str(A * B * C)))

# 0~9 사이의 숫자로 Counter 결과를 조회한다. 없는 경우 0을 출력한다.
for num in range(10):
    if str(num) in result:
        print(result[str(num)])
    else:
        print(0)
