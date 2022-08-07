
'''
Solution 1:
Time Complexity: O(n)
Space Complexity: O(1)
'''
def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < len(s) and not s[left].lower().isalnum():
                left += 1
            while right >= 0 and not s[right].lower().isalnum():
                right -= 1
            if left < len(s) and right >= 0:
                if s[left].lower() != s[right].lower():
                    return False
            left += 1
            right -= 1
        return True

'''
Solution 2:
Time Complexity: O(n)
Space Complexity: O(n) -> could do it in O(1) @TODO
'''
def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = re.sub(r'[^\w\\s]|_', '', s)
        left = 0
        right = len(a) - 1
        while left < right:
            if a[left] != a[right]:
                return False
            left += 1
            right -= 1
        return True