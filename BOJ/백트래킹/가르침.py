N, K = map(int, input().split())
# 단아의 학습 여부를 나타내는 딕셔너리
readable = {
    "a": 1, "b": 0, "c": 1, "d": 0, "e": 0, "f": 0,
    "g": 0, "h": 0, "i": 1, "j": 0, "k": 0, "l": 0,
    "m": 0, "n": 1, "o": 0, "p": 0, "q": 0, "r": 0,
    "s": 0, "t": 1, "u": 0, "v": 0, "w": 0, "x": 0,
    "y": 0, "z": 0,
}
alphabets = list(readable.keys())

words = []
for _ in range(N):
    # "anta"와 "tica"를 제외한 단어만 담는다.
    words.append(input()[4:-4])


def combination(path, index, count):
    global max_count

    # 배울 수 있는 만큼 다 배우면,
    if count >= K - 5:
        readable_count = 0
        # 모든 단어에 대해 읽기 가능 여부를 판단한다.
        for word in words:
            is_readable = True
            # 단어를 구성하는 모든 문자를 읽을 수 있는지 확인한다.
            for char in word:
                if not readable[char]:
                    is_readable = False
                    break

            if is_readable:
                readable_count += 1

        max_count = max(max_count, readable_count)
        return

    # 아직 배우지 않은 알파벳에 대해 조합을 구성한다.
    for idx in range(index, len(alphabets)):
        current = alphabets[idx]

        if not readable[current]:
            readable[current] = 1
            combination(path + [current], idx + 1, count + 1)
            readable[current] = 0


# K가 5보다 작으면 기본적으로 포함되는 'a','c','n','i','t'를 배울 수 없다.
if K < 5:
    print(0)
else:
    max_count = 0
    combination([], 0, 0)

    print(max_count)
