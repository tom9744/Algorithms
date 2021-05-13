import sys

from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    P = list(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline().rstrip())
    array = sys.stdin.readline().rstrip()[1:-1]

    if len(array) > 0:
        numbers = deque(array.split(","))
    else:
        numbers = deque([])

    is_error = False
    deletion_from_front = True

    for command in P:
        if command == "R":
            deletion_from_front = not deletion_from_front
        elif command == "D":
            if not numbers:
                is_error = True
                break

            if deletion_from_front:
                numbers.popleft()
            else:
                numbers.pop()

    if is_error:
        print("error")
    elif deletion_from_front:
        print(f"[{','.join(numbers)}]")
    else:
        print(f"[{','.join(reversed(numbers))}]")