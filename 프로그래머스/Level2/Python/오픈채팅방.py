from collections import defaultdict


def solution(records):
    user_table = defaultdict(str)
    log = []
    answer = []

    # commmands[0]: 행동 / commmands[1]: 아이디 / commmands[2]: 별명
    for record in records:
        commands = record.split()

        if commands[0] == "Leave":
            log.append([commands[1], "out"])
            continue

        # 아이디와 닉네임을 매핑한다.
        user_table[commands[1]] = commands[2]

        if commands[0] == "Enter":
            log.append([commands[1], "in"])
        elif commands[0] == "Change":
            user_table[commands[1]] = commands[2]

    for line in log:
        user_id, direction = line

        if direction == "in":
            answer.append(f"{user_table[user_id]}님이 들어왔습니다.")
        else:
            answer.append(f"{user_table[user_id]}님이 나갔습니다.")

    return answer
