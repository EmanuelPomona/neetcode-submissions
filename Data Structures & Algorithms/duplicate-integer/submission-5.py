class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False





def containtsdup(s):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False
    






















class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a datastrcture that allows us to store values we've seen already
        seen = set()

        for num in nums:
            if num in seen:
                return True
            # have to add the num to the list regardless
            seen.add(num)
        # need to return false as a defult value
        return False