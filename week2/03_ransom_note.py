'''
Solution 1:
let n = # chars in magazine
let m = # chars in ransomNote
Time complexity: O(n + m)
Space complexity: O(1)
'''
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_frequencies = [0] * 26
        for char in ransomNote:
            letter_frequencies[ord(char) - ord('a')] += 1
        
        for char in magazine:
            letter_frequencies[ord(char) - ord('a')] -= 1
        
        for l in letter_frequencies:
            if l > 0:
                return False
        
        return True
