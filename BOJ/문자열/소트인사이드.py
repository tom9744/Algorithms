N = input()

# 파이썬의 내장 정렬함수는 팀 소트로, 최악 시간 복잡도가 O(logN)이다.
print("".join(sorted(list(N), reverse=True)))
