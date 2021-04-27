K = int(input())
numbers = []

# 스택으로 구현하여, 0이 나올 때마다 맨 위의 값을 빼면 된다.
for _ in range(K):
    number = int(input())

    if number == 0:
        numbers.pop()
    else:
        numbers.append(number)

print(sum(numbers))