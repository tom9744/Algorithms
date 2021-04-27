def using_replace():
    word = input()

    croatian_alpha = [
        "c=", "c-", "dz=", "d-",
        "lj", "nj", "s=", "z="
    ]

    # 크로아티아 알파벳에 해당하는 부분문자열을 "*"로 바꾼다.
    for each in croatian_alpha:
        word = word.replace(each, "*")

    # 문자열의 길이를 출력한다.
    print(len(word))


def using_slicing():
    word = input()

    croatian_alpha = [
        "c=", "c-", "dz=", "d-",
        "lj", "nj", "s=", "z="
    ]
    count = 0

    while word:
        # 길이가 2인 부분 문자열에 대해 크로아티아 알파벳 여부를 판별한다.
        if word[:2] in croatian_alpha:
            count += 1
            # 크로아티아 알파벳인 경우, 문자열 앞에서 길이 2만큼 자르고 재할당한다.
            word = word[2:]
            continue
        # 길이가 3인 부분 문자열에 대해 크로아티아 알파벳 여부를 판별한다.
        if word[:3] in croatian_alpha:
            count += 1
            # "dz="인 경우, 문자열 앞에서 길이 3만큼 자르고 재할당한다.
            word = word[3:]
            continue

        # 크로아티아 알파벳이 아닌 경우, 문자열 앞에서 길이 1만큼 자르고 재할당한다.
        count += 1
        word = word[1:]

    print(count)
