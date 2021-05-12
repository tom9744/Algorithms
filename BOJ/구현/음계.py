scale = map(int, input().split())

start = scale[0]

if start == 0:
    for _, sound in enumerate(scale, 1):
        if abs(start - sound) > 1:
            print("mixed")
            return
    print("ascending")
    return

elif start == 8:
    for _, sound in enumerate(scale, 1):
        if abs(start - sound) > 1:
            print("mixed")
            return
    print("descending")
    return
