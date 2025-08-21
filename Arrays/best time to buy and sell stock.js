//given array price where price[i] is the price of a given stock on ith day.
//You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
//find the maximum profit you can achieve from this transaction.
//If you cannot achieve any profit, return 0.
//You must buy before you sell, so you cannot buy and sell on the same day.

function maxProfit(prices) {
  let minPrice = prices[0]; // Initialize minimum price to the first element
  let maxProfit = 0; // Initialize maximum profit to 0

  for (let i = 1; i < prices.length; i++) {
    if (prices[i] < minPrice) {
      minPrice = prices[i]; // Update minimum price if current price is lower
    } if (prices[i] - minPrice > maxProfit) {
      maxProfit = prices[i] - minPrice; // Update maximum profit if current profit is higher
    }
  }

  return maxProfit; // Return the maximum profit found
}

let prices = [700, 100, 50, 30, 60, 10, 4];
console.log(maxProfit(prices)); // Output: 30 (Buy on day 4 at price 30 and sell on day 5 at price 60)
let prices2 = [7, 6, 4, 3, 1];
console.log(maxProfit(prices2)); // Output: 0 - No profit
let prices3 = [1, 2, 3, 4, 5];
console.log(maxProfit(prices3)); // Output: 4 (Buy on day 1 at price 1 and sell on day 5 at price 5)

