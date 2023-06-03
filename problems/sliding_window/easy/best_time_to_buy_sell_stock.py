# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# input: prices = [7,1,5,3,6,4]
# output: 5

# sliding window:
def maxProfit(prices):
    left = 0
    right = 1
    maxProfit = 0

    while right < len(prices):
        # profitable?
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left] # simply calculate profit and update maxProfit
            maxProfit = max(profit, maxProfit)
        else:
            # we want left to be low
            left = right
        
        right += 1

    return maxProfit

# O(n) time
# O(1) space