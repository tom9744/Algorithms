# 2810 : 컵홀더
#
# 커플석 LL이 한 개도 없는 경우, 컵 홀더의 개수는 의자 개수 + 1이다. (답 : max_num_of_holders - 1)
# 커플석 LL이 하나 존재할 때 마다, 존재할 수 있는 컵 홀더의 수가 하나씩 줄어든다.
# 따라서 커플석 개수를 세고, 그 값을 컵 홀더 개수 최대 값 (의자 개수 + 1)에서 빼면 된다.


def count_num_of_couple_seats(seats):
    array = seats.split('S')
    count = 0

    for item in array:
        count += len(item) // 2 if len(item) > 0 else 0

    return count


num_of_seats = int(input())
seats = input()
max_num_of_holders = len(seats) + 1
couple_seats = count_num_of_couple_seats(seats)

print(max_num_of_holders - couple_seats if couple_seats > 0 else max_num_of_holders - 1)
