N = int(input())
words = list(set([input() for _ in range(N)]))
words.sort(key=lambda word: [len(word), word])

for each in words:
    print(each)
