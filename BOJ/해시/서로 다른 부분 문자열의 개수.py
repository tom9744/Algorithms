S = input()
hash_table = {}

for i in range(len(S)):
    for j in range(len(S) - i):
        substring = S[j:j + i + 1]  # 부분 문자열을 구한다.
        hash_table[substring] = True       # 해시 테이블의 Key 값으로 사용한다.

print(len(hash_table.keys()))  # 해시 테이블의 Key 개수를 반환한다.
