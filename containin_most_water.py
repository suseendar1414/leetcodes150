# You are given an integer array heights where heights[i] represents the height of the ith bar
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36
height = [1,7,2,5,4,7,3,6]

from typing import List

class Solution:
    def contMostwater(self,height: List[int]):
        left = 0
        right = len(height) - 1

        max_area = 0
        while left < right:
            wid = right - left
            hei = min(height[left],height[right])
            area = wid * hei
            max_area = max(max_area,area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    
solution = Solution()
result = solution.contMostwater(height)
print(result)
            