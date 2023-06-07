# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# input: prices = [7,1,5,3,6,4]
# output: 5

# this is not exactly the 'Sliding Window' technique
# we take adventadge of the nature of the problem. We should always compare a num to another to the RIGHT
# since we need to buy before selling. we want to buy at LOWEST and sell at HIGHEST, but in the right -> direction
def maxProfit(prices):
    left = 0
    right = 1
    maxProfit = 0

    while right < len(prices):
        if prices[left] < prices[right]: # profitable?
            profit = prices[right] - prices[left]   # simply calculate profit
            maxProfit = max(profit, maxProfit)      # and update maxProfit
        else:
            # we want left to always be the lowest possible, so we move the left pointer all the way to the right pos
            left = right
        
        right += 1  # We keep moving the right pointer through the end of the array, regardless

    return maxProfit

# O(n) time
# O(1) space