class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Optimal O(N)
        
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            if prices[l] > prices[r]:
                l = r
            r += 1

        return max(0, max_profit)
        
        
        #Brute Force O(N^2)
        '''max_profit = 0
        for i in range(len(prices)):
            
            for j in range(i+1, len(prices)):
                
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
        return max(0, max_profit)'''
