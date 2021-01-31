# 2920 : 음계
#
# 왜 틀린지 모르겠음....;;;


def is_ascending(play):
    if play[0] != 1:
        return False

    prev = play.pop(0)

    for note in play:
        if prev == note - 1:
            prev = note
        else:
            return False
    return True


def is_descending(play):
    if play[0] != 8:
        return False

    prev = play.pop(0)

    for note in play:
        if prev == note + 1:
            prev = note
        else:
            return False
    return True


music = list(map(int, input().split()))

if is_ascending(music):
    print("ascending")
elif is_ascending(music):
    print("descending")
else:
    print("mixed")
