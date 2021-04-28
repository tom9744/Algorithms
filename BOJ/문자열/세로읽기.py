# 내장함수 zip()을 사용하면 ['A', 'B', 'C'], ['D', 'E']일 때,
# [('A', 'D'), ('B', 'E')]와 같이 가장 짧은 길이의 배열을 기준으로 나머지는 잘리게 된다.
#
# itertools.zip_longest()를 사용하면 가장 긴 길이의 배열을 기준으로
# [('A', 'D'), ('B', 'E'), ('C', None)]과 같은 결과를 반환하며,
# 두번째 인자에 대체할 값을 넣어주면 None 대신 그 값으로 채워진다.
from itertools import zip_longest

words = [list(input()) for _ in range(5)]

# 길이가 부족한 배열의 빈 공간을 None 대신 빈 문자열 ''로 채운다.
for col in zip_longest(*words, fillvalue=''):
    print("".join(col), end='')
