'''
Solution 1:
Time complexity: O(n)
Space compleity: O(n)
top down
'''
def __init__(self):
        self.solution = {}
def climbStairs(self, n: int) -> int:
	if n in self.solution:
	    return self.solution[n]
	if n == 1:
	    self.solution[1] = 1
	    return 1
	if n == 2:
	    self.solution[2] = 2
	    return 2
	result = self.climbStairs(n - 2) + self.climbStairs(n - 1)
	self.solution[n] = result
	return result

'''
Solution 2:
Time complexity: O(log(n))  <- based on the built in math.pow function
Space complexity: O(log(n)) <- based on the built in math.pow function
'''
def climbStairs(self, n: int) -> int:
	phi = 1.618033988749894
	return round(math.pow(phi, (n + 1)) / sqrt(5))

'''
Solution 3:
Time complexity: O(n)
Space complexity: O(n)
bottom up
'''
def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        memo = [0] * n
        memo[0] = 1
        memo[1] = 2
        for i in range(2, n):
            memo[i] = memo[i-1] + memo[i-2]
        
        return memo[n - 1]
