### brutal forces
def maxProfit(prices: list) -> int:
    max_profit = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)

    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))

