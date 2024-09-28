# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?

# Example 1:
# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

# Output: true

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # print(matrix)
        if not matrix or not matrix[0]:
            return False
        m,n = len(matrix), len(matrix[0])
        start = 0
        stop = m * n - 1
        while start <= stop:
            mid = (start + stop) // 2
            row = mid // n
            col = mid % n
            mid_value = matrix[row][col]
            if mid_value == target:
                return True
            elif target > mid_value:
                start = mid + 1
            else :
                stop = mid - 1
        return False



solution = Solution()
result = solution.searchMatrix(matrix,target)
print(result)