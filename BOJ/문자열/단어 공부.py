from collections import Counter

# 단어를 구성하는 알파벳의 빈도수를 세고, 오름차순 정렬한다. (모두 대문자로 변경)
candidates = Counter(list(input().upper())).most_common()

# 길이가 2보다 긴 경우, 상위 2개를 뽑아 빈도수를 비교한다.
if len(candidates) > 1:
    first, second = candidates[:2]

    # 빈도수가 같으면 ?를 출력한다.
    if first[1] == second[1]:
        print("?")
    # 빈도수가 다르면 더 큰 문자를 출력한다.
    else:
        print(first[0])
# 길이가 2보다 작은 경우, 맨 앞의 것을 출력한다.
else:
    print(candidates[0][0])
