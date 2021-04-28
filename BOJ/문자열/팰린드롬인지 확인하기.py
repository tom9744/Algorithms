word = input()

# word[::-1]는 배열의 복사본을 생성해 뒤집는다. 즉, 같으면 팰린드롬이다.
print(1 if word == word[::-1] else 0)
