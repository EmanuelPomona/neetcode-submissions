
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



        



class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = s.lower()
        result = ""

        for char in news:
            if char.isalnum():
                result += char

        i = 0
        j = len(result) - 1

        while i < j:
            if result[i] != result[j]:
                return False
            
            i += 1
            j -= 1
        
        return True












