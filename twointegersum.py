# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Input: 
nums = [3,4,5,4]
target = 8

# Output: [0,1]

from typing import List


class Solution():
    def twosum(self,nums: List[int], target: int):
       res = {}
       for i,num in enumerate(nums):
        #    print(i)
           diff =  target - num
           if diff in res:
               return (res[diff],i)
           res[num] = i

solution = Solution()
result = solution.twosum(nums,target)
print(result)