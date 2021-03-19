# 코딩테스트 연습 > 스택/큐 > 주식가격 (Level2)
def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer[i] += 1
                break
            else:
                answer[i] += 1

    return answer


print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]
