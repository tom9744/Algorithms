import bisect

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()  # 이진 검색을 위해 정렬한다.

M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    # bisect_left 메서드로 target 값이 삽입될 수 있는 인덱스를 찾는다.
    index = bisect.bisect_left(numbers, target)

    # 얻은 인덱스 위치에 존재하는 값이 target 값과 일치하고, 배열 범위 내에 있는지 확인한다.
    if index < len(numbers) and numbers[index] == target:
        print(1)
    else:
        print(0)
