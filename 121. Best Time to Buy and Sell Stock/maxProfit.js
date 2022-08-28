/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    var buy = prices[0]
    var profit = 0
    prices.forEach(function(p){
        buy = Math.min(buy,p)
        profit = Math.max(profit, p-buy)
    });
    return profit
};

// Runtime 107 ms / Memory 51.8 MB
// debug: https://jsfiddle.net/