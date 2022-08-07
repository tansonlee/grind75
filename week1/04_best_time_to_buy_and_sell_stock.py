
'''
Solution 1:
Time Complexity: O(n^2)
Space Complexity: O(1)
'''
def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)):
            for j in range(0, i):
                high_price = prices[i]
                low_price = prices[j]
                if high_price - low_price > result:
                    result = high_price - low_price
        return result


'''
Solution 1:
Time Complexity: O(n)
Space Complexity: O(1)
'''
def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        profit = 0
        for p in prices:
            if p - lowest > profit:
                profit = p - lowest
            if p < lowest:
                lowest = p
        return profit