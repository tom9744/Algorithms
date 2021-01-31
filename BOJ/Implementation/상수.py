A, B = map(list, input().split())

A.reverse()
B.reverse()

reversedA = int("".join(A))
reversedB = int("".join(B))

print(max(reversedA, reversedB))
