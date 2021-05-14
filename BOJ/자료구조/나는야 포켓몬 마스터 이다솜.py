import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
dict_by_num = {}
dict_by_name = {}

for num in range(1, N + 1):
    pokemon = sys.stdin.readline().rstrip()

    dict_by_num[num] = pokemon   # 포켓몬 번호를 Key 값으로 사용해 딕셔너리 구성
    dict_by_name[pokemon] = num  # 포켓몬 이름을 Key 값으로 사용해 딕셔너리 구성

for _ in range(M):
    command = sys.stdin.readline().rstrip()

    # 입력값의 숫자/문자 여부에 따라 알맞는 딕셔너리 조회
    if command.isdigit():
        print(dict_by_num[int(command)])
    else:
        print(dict_by_name[command])
