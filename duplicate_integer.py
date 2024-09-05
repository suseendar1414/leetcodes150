# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Input: nums = [1, 2, 3, 3]

# Output: true
nums = [1, 2, 3]
from typing import List

class Solution:
    def hashDuplicate(self, nums: List[int]):
        res = {}
        for i in range(len(nums)):
            res[nums[i]] = (res.get(nums[i],0) + 1)
            for n in res.values(): 
                if n  > 1:
                    return True
        return False
        
            

solution = Solution()
result = solution.hashDuplicate(nums)

