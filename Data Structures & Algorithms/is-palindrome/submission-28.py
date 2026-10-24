class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = s.lower()
        word = ""
        for char in new:
            if char.isalnum():
                word += char

        left = 0
        right = len(word)-1

        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        
        return True
        