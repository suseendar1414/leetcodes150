# Search in a sorted infinite array
# Given an infinite sorted array (or an array with unknown size), find if a given target value is present in the array. Write a function to return the index of the target if it is present in the array, otherwise return -1.

# Example 1:

# Input: [2, 5, 7, 9, 10, 12, 15, 16, 18, 20, 24, 28. 32, 35], target = 16
# Output: 7
# Explanation: The target is present at index '7' in the array.

nums = [2, 5, 7, 9, 10, 12, 15, 16, 18, 20, 24, 28, 32, 35]
target = 16

class Solution:
    def posofinf(self,nums, target):
        start = 0
        end =  1
        while True:
            if nums[end] < target:
                start = end + 1
                end = end * 2
            else:
                break

        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1    
            else :
                stop = mid - 1
        return mid


solution = Solution()
result = solution.posofinf(nums,target)
print(result)

