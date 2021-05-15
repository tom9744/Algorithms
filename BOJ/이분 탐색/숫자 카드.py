from collections import defaultdict


# 해시 자료구조를 이용한 풀이
def solution_hash(cards, targets):
    hash_table = defaultdict(int)

    for card in cards:
        hash_table[card] = 1

    for target in targets:
        print(1 if hash_table[target] else 0, end=" ")


# 이진 검색을 이용한 풀이
def solution_binary_search(cards, targets):
    sorted_cards = sorted(cards)

    for target in targets:
        is_found = False
        start, end = 0, len(sorted_cards) - 1

        while start <= end:
            mid = (start + end) // 2

            if sorted_cards[mid] < target:
                start = mid + 1
            elif sorted_cards[mid] > target:
                end = mid - 1
            else:
                is_found = True
                break

        print(1 if is_found else 0, end=" ")


if __name__ == '__main__':
    N = int(input())
    cards = list(map(int, input().split()))
    M = int(input())
    targets = list(map(int, input().split()))

    solution_hash(cards, targets)           # Memory: 107MB, Runtime: 2460ms
    solution_binary_search(cards, targets)  # Memory: 136MB, Runtime: 908ms
