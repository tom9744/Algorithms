from collections import Counter

N = int(input())
books = [input() for _ in range(N)]
sales = list(Counter(books).items())

# 판매수는 내림차순, 제목은 사전식 오름차순 정렬한다.
sales.sort(key=lambda elem: (-elem[1], elem[0]))

print(sales[0][0])
