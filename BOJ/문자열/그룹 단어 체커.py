from collections import defaultdict

N = int(input())
count = 0

for _ in range(N):
    word = input()

    # 빈 문자열 예외처리
    if not word:
        continue

    freq = defaultdict(int)
    freq[word[0]] = 1  # 시작 문자 초기화

    # 앞 문자와 뒷 문자가 다른 경우, 해당 문자의 등장 빈도수 증가
    for idx in range(len(word) - 1):
        if word[idx] != word[idx + 1]:
            freq[word[idx + 1]] += 1

    # 최대 빈도수가 1인 경우, 그룹 단어로 판단
    if max(freq.values()) == 1:
        count += 1

print(count)