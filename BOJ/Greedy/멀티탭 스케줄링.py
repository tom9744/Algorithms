# 1700 : 멀티탭 스케줄링
#
# 조건 분기를 통해, 다음 케이스에 대해 각기 다른 처리를 수행해야 한다.
#
# 1. 해당 전자기기가 멀티탭에 꽂혀있는 경우
# 2. 해당 전자기기가 멀티탭에 꽂혀있지 않은 경우
#   2-1. 멀티탭에 자리가 남은 경우
#   2-2. 멀티탭에 자리가 남지 않은 경우
#       2-2-1. 현재 멀티탭에 꽂혀 있는 전자기기가 전부 다음에 다시 사용해야 하는 경우
#       2-2-2. 현재 멀티탭에 꽂혀 있는 전자기기 중 다시 사용할 예정이 없는 기기가 있는 경우

N, M = map(int, input().split())
sequence = list(map(int, input().split()))
multi_tap = []
count = 0

while len(sequence) != 0:
    current_task = sequence.pop(0)

    is_using = True if multi_tap.count(current_task) > 0 else False

    # 멀티탭 이미 해당 전자기기가 사용중인 경우
    if is_using:
        continue
    else:
        # 멀티탭에 자리가 남아있는 경우
        if len(multi_tap) < N:
            multi_tap.append(current_task)
        else:
            target = 0
            most_last_use = 0
            has_changed = False

            for position in range(N):
                try:
                    # 가장 나중에 다시 쓰이는 전자기기의 멀티탭 상 위치를 찾는다
                    next_usage = sequence.index(multi_tap[position])
                    if most_last_use < next_usage:
                        most_last_use = next_usage
                        target = position
                except:
                    # 나중에 다시 쓰이지 않는 전자기기가 있는 경우
                    has_changed = True
                    count += 1
                    multi_tap.pop(position)
                    multi_tap.append(current_task)
                    break

            if not has_changed:
                count += 1
                multi_tap.pop(target)
                multi_tap.append(current_task)

print(count)

