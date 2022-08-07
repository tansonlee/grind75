
'''
Solution 1:
Time Complexity: O(n)
Space Complexity: O(n)
'''
def isValid(self, s: str) -> bool:
  stack = []
  for char in s:
    if char == '(' or char == '{' or char == '[':
      stack.append(char)
    elif char == ')' or char == ']' or char == '}':
      if len(stack) == 0:
        return False
      top = stack.pop()
      if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
        return False
  return len(stack) == 0

'''
Solution 2:
Restriction: The only datastructure that can be used is a queue.
Time Complexity: O(n^2)
Space COmplexity: O(n)
'''
from collections import deque

class Stack:
  def __init__(self):
    self.queue = deque()
    self.size = 0
  def push(self, value):
    self.queue.append(value)
    for i in range(self.size):
      e = self.queue.popleft()
      self.queue.append(e)
    self.size += 1
  def pop(self):
    self.size -= 1
    return self.queue.popleft()
  def length(self):
    return self.size
        
def isValid(self, s: str) -> bool:
  stack = Stack()
  for char in s:
    if char == '(' or char == '{' or char == '[':
      stack.push(char)
    elif char == ')' or char == ']' or char == '}':
      if stack.length() == 0:
        return False
      top = stack.pop()
      if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
        return False
  return stack.length() == 0

