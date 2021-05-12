scale = list(map(int, input().split()))
prev = scale[0]

if prev == 1:
    for _, sound in enumerate(scale, 1):
        if abs(prev - sound) > 1:
            print("mixed")
            exit(0)
        prev = sound
    print("ascending")
elif scale[0] == 8:
    for _, sound in enumerate(scale, 1):
        if abs(prev - sound) > 1:
            print("mixed")
            exit(0)
        prev = sound
    print("descending")
else:
    print("mixed")
