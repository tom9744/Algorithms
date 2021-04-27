N, M = map(int, input().split())
have_not_heard = set([input() for _ in range(N)])
have_not_seen = set([input() for _ in range(M)])
have_not_heard_and_seen = have_not_heard & have_not_seen  # 두 집합의 교집합

# 교집합 원소의 개수와 각 원소를 사전순으로 정렬해 하나씩 출력
print(len(have_not_heard_and_seen))
for each in sorted(list(have_not_heard_and_seen)):
    print(each)
