class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1

        output = [0]*2

        while i < j:
            csum = numbers[i] + numbers [j]

            if csum == target:
                return [i+1, j+1]
            if csum < target:
                i += 1
            else:
                j -= 1

