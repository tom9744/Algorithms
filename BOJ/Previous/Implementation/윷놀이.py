for _ in range(3):

    yuts = list(map(int, input().split()))
    back = sum(yuts)

    if back == 0:
        print("D")
    elif back == 1:
        print("C")
    elif back == 2:
        print("B")
    elif back == 3:
        print("A")
    elif back == 4:
        print("E")