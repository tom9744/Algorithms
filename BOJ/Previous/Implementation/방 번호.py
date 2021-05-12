# 1475 : 방 번호
#
# 각 번호를 인덱스로 가지는 배열을 선언하고, 원소를 해당 번호를 사용할 수 있는 횟수로 생각한다.
# 즉, 모든 번호를 1번씩 사용할 수 있는 초기상태는 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]이다.
#
# 주어진 방 번호에 대해 반복문을 수행하면서 등장하는 숫자의 인덱스에 위치한 사용가능 횟수를 -1 한다.
# 즉, 숫자 2가 나오는 경우 배열의 2번째 인덱스에 있는 값이 -1 되어, [1, 1, 0, 1, 1, 1, 1, 1, 1, 1]과 같이 된다.
#
# 이미 해당 위치의 사용 가능 횟수가 0인 경우, 새로운 세트를 구매한 것으로 가정하고 전체 배열 원소에 각각 +1 해준다.
# 즉, 숫자 2가 다시 나오면 배열의 상태는 [2, 2, 1, 2, 2, 2, 2, 2, 2, 2]와 같이 된다.
#
# 이렇게 반복하면 필요한 숫자 세트의 개수를 구할 수 있다.


def purchase_new_set(array):
    new_array = []
    for each in array:
        new_array.append(each + 1)

    return new_array


N = list(map(int, list(input())))

# 사용 가능 횟수 : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
possible = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
count = 1

for each in N:
    if possible[each] == 0:
        if each == 6:
            if possible[9] != 0:
                possible[9] -= 1
                continue
        elif each == 9:
            if possible[6] != 0:
                possible[6] -= 1
                continue
        count += 1
        possible = purchase_new_set(possible)  # 새로운 숫자 세트 구매

    possible[each] -= 1

print(count)