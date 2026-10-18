class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            j = len(nums)-1
            k = i + 1

            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            while k < j:
                current = nums[i] + nums[j] + nums[k]
                if current == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    j-= 1
                    k+= 1

                    while k < j and nums[k] == nums[k-1]:
                        k+= 1
                    
                    while k < j and nums[j] == nums[j+1]:
                        j-= 1
                
                if current > 0:
                    j-= 1
                elif current < 0:
                    k+= 1
        
        return result
                


