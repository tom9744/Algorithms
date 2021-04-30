def main():
    N = int(input())

    for seq_num in range(1, N + 1):
        words = input().split(" ")

        # 스택을 사용한 풀이
        reversed_words = []

        while words:
            reversed_words.append(words.pop())

        print(f"Case #{seq_num}: {' '.join(reversed_words)}")

        # 내장 메서드를 사용한 풀이
        print(f"Case #{seq_num}: {' '.join(reversed(words))}")


if __name__ == '__main__':
    main()