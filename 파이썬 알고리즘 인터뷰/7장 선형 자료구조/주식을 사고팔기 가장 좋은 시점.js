// 나의 풀이 (Runtime: 112ms, Memory: 48.7MB)
const maxProfit = function(prices) {
  let maxProfit = -Infinity;
  let minPrice = prices[0];
   
  prices.forEach(price => {
    minPrice = Math.min(minPrice, price);
    maxProfit = Math.max(maxProfit, price - minPrice);
  });
   
  return maxProfit;
};