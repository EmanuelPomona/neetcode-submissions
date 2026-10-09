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













#Trying Again
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for char in s:
            if char.isalnum():
                new += char
        
        new = new.lower()

        left = 0
        right = len(new) - 1

        while left < right:
            if new[left] != new[right]:
                return False
            
            left += 1
            right -= 1
        
        return True



        