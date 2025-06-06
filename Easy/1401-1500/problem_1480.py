# only if you run outside leetcode
# from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        result[0] = nums[0]

        for i in range(1,len(nums)):
            result[i] = result[i-1] + nums[i]
        return result

# only if you run outside leetcode
# print(Solution().runningSum([1, 2, 3, 4]))
