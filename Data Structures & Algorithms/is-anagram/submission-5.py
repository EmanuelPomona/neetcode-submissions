class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}
        for char in (s):
            if char not in s1:
                s1[char] = 1
            else:
                s1[char] += 1
        for char in (t):
            if char not in s2:
                s2[char] = 1
            else:
                s2[char] += 1
        return s1 == s2
            
        






class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Dictionary will map char and frequency
        s1 = {}
        t1 = {}

        for char in s:
            if char in s1:
                s1[char] += 1
            else:
                s1[char] = 0
        
        for char in t:
            if char in t1:
                t1[char] += 1
            else:
                t1[char] = 0
        
        return s1 == t1





