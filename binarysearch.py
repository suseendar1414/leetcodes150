# You are given an array of distinct integers nums, sorted in ascending order,
#  and an integer target.

# Implement a function to search for target within nums. 
# If it exists, then return its index, otherwise, return -1.

# Your solution must run in 
# O(logn) time.

# Input: nums = [-1,0,2,4,6,8], target = 4
nums = [-1,0,2,4,6,8]
target = 4
# Output: 3


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # print(target)
        start = 0
        stop = len(nums) - 1
        while start <= stop:
            mid = (start + stop)//2
            if nums[mid] == target:
                return True
            elif target > nums[mid]:
                start = mid +1
            else :
                stop = mid -1   

        return False         

# from typing import List

# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
#         start = 0
#         stop = len(nums) - 1
        
#         while start <= stop:
#             mid = (start + stop) // 2  # Integer division to get the middle index
#             if nums[mid] == target:
#                 return True  # Return True when the target is found
#             elif target > nums[mid]:
#                 start = mid + 1  # Search in the right half
#             else:
#                 stop = mid - 1  # Search in the left half
        
#         return False  # Return False if the target is not found



solution = Solution()
result = solution.search(nums,target)
print(result)
