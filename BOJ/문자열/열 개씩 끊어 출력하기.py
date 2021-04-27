def new_answer():
    string = input()

    for n in range(10):
        # 10칸 씩 범위를 이동하며 문자열을 자른다.
        start = 10 * n
        end = (10 * n) + 10
        partition = string[start:end]

        # 문자열을 자른 결과가 빈 문자열 ""인 경우, 종료한다.
        if not partition:
            break

        print(partition)


# 2달 전 (2021년 2월)에 작성한 풀이
def prev_answer():
    import sys

    N = list(sys.stdin.readline().rstrip())
    temp = []

    for idx in range(len(N)):
        if idx != 0 and idx % 10 == 0:
            print("".join(temp))
            temp = []

        temp.append(N[idx])

    if len(temp) > 0:
        print("".join(temp))


new_answer()   # 슬라이싱을 이용한 파이썬 다운 풀이
prev_answer()  # 언어만 파이썬일 뿐, 언어의 특색을 살리지 못한 풀이
