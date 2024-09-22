# Given an array of integers nums, return the length of the longest consecutive sequence of elements.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

# You must write an algorithm that runs in O(n) time.


# Input: nums = [2,20,4,10,3,4,5]

# Output: 4

nums = [2,20,4,10,3,4,5]

from typing import List

class Solution:
    def longSeq(self, nums: List[int]):
        numset = set(nums)
        output = 0
        for i in numset:
            if (i - 1) not in numset:
                length = 1
                while (i + length) in numset:
                    length += 1
                output = max(output,length)
        return output
    
        
solution = Solution()
result = solution.longSeq(nums)
print(result)