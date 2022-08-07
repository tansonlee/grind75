'''
Solution 1:
Time Complexity: O(n^2)
Space Complexity: O(1)
'''

def twoSum(self, nums: List[int], target: int) -> List[int]:
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]

'''
Solution 2:
Time Complexity: O(n)
Space Complexity: O(n)
Datastructure: Dictionary
'''

def twoSum(self, nums: List[int], target: int) -> List[int]:
  memo = {}
  for i in range(len(nums)):
    current = nums[i]
    desired = target - current
    if desired in memo:
      return [i, memo[desired]]
    memo[current] = i
