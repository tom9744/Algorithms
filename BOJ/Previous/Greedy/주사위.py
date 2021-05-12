# 1041 : 주사위
#
# 주어진 주사위들로 만들 수 있는 정육면체에서 각각 1, 2, 3개의 면이 노출되는 주사위 개수를 구한다.
# 또한, 주어진 주사위 하나에서 각각 1, 2, 3개의 면에 적혀있는 수의 합이 최소가 되는 경우도 구한다.
# 1, 2, 3개 면에 대해 구한 최소값과 개수를 곱해 답을 구한다.

N = int(input())
A, B, C, D, E, F = map(int, input().split())
array = [A, B, C, D, E, F]

if N == 1:
    array.sort()
    print(sum(array) - array[-1])
else:
    single_min = min(array)
    double_min = min(list(map(sum, ([A, B], [A, C], [A, D], [A, E], [B, C], [B, D], [B, F], [C, E], [C, F], [D, E], [D, F], [E, F]))))
    triple_min = min(list(map(sum, ([A, B, C], [A, B, D], [A, D, E], [A, C, E], [F, B, D], [F, B, C], [F, D, E], [F, E, C]))))

    single_sided = (5 * N * N) - (16 * N) + 12
    double_sided = (8 * N) - 12
    triple_sided = 4

    single_sided_sum = single_sided * single_min
    double_sided_sum = double_sided * double_min
    triple_sided_sum = triple_sided * triple_min

    print(single_sided_sum + double_sided_sum + triple_sided_sum)


