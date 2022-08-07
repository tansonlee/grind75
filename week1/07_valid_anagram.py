'''
Solution 1
Time Complexity: O(n)
Space Complexity: O(n)
'''
def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        scounts = {}
        for char in s:
            if char in scounts:
                scounts[char] += 1
            else:
                scounts[char] = 1
        
        tcounts = {}
        for char in t:
            if char in tcounts:
                tcounts[char] += 1
            else:
                tcounts[char] = 1
        
        for char in scounts:
            if char not in tcounts:
                return False
            if scounts[char] != tcounts[char]:
                return False
        
        for char in scounts:
            if char not in scounts:
                return False
            if tcounts[char] != scounts[char]:
                return False

        return True