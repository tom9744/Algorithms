def find_subset(path, index):
    # 길이가 1 이상, 합이 S인 부분집합을 배열에 담는다.
    if len(path) > 0 and sum(path) == S:
        subsets.append(path)

    for i in range(index, N):
        find_subset(path + [numbers[i]], i + 1)


N, S = map(int, input().split())
numbers = list(map(int, input().split()))
subsets = []

find_subset([], 0)

print(len(subsets))
