S = input()
# 접미사를 배열에 저장한다. (리스트 컴프리헨션)
suffixes = [S[start:] for start in range(len(S))]

for suffix in sorted(suffixes):
    print(suffix)

