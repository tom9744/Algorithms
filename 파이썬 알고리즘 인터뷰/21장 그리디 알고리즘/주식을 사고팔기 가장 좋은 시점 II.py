from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for idx in range(len(prices) - 1):
            price, next_price = prices[idx], prices[idx + 1]

            # 내일 가격이 오르는 경우, 구매하고 즉시 판매한다.
            # [1, 3, 5] 같이 계속 오르는 경우, 사고팔고를 반복하면 결국 똑같다.
            if price < next_price:
                profit += next_price - price

        return profit
