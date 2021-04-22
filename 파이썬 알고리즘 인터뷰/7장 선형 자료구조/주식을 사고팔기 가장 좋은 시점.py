import sys 

class Solution:
    # 나의 풀이 (Runtime: 972ms, Memory: 25MB)
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # 최저가를 첫 번째 가격으로 초기화한다.
        minimum_price = prices[0]
        maximum_profit = sys.minsize
        
        for idx, price in enumerate(prices):
            # 더 낮은 가격이 존재하는 경우, 최저가를 교체한다.
            if price < minimum_price:
                minimum_price = price
            
            # 최저가로 구매한 경우 얻을 수 있는 이익으로 배열을 갱신한다.
            prices[idx] = prices[idx] - minimum_price
        
        # 배열에서 최대값을 찾아 출력한다.
        return max(prices)