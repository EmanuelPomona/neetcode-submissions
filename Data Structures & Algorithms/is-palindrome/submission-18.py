


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newstr = ""
        for char in s:
            if char.isalnum():
                newstr += char
        
        newstr = newstr.lower()

        right = len(newstr)-1
        left = 0

        while left < right:
            if newstr[left] != newstr[right]:
                return False
            right -= 1
            left += 1
        return True



        