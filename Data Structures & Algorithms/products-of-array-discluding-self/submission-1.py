class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        output = n * [1]
        prefix = n * [1]
        suffix = n * [1]

        product = 1
        for i in range(len(nums)):
            prefix[i] = product
            product *= nums[i]

        product = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = product
            product *= nums[i]
        
        for i in range(len(nums)):
            current = prefix[i] * suffix[i]
            output[i] = current


        return output

        