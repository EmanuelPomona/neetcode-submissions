class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest = 0
        i = 0
        j = len(heights)-1

        while i < j:
            area = (j - i) * (min(heights[i], heights[j]))
            if area > biggest:
                biggest = area
            if heights[i] > heights[j]:
                j-= 1
            else:
                i+= 1
        
        return biggest
        

# how do we maximize area?
#Max area = highest length * highest width)
#how do we get the highest values for length and width?
# start with. max width then slowly go down
# 


#Method 1: Find all combiantions of area
    # not efficient
#Method 2: 


#Formual:
    # width = (j - i)
    # height = min(j, i)

#Find the width from the furthers and get smaller and have 


