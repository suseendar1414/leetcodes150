nums = [1,2,4,6]
from typing import List


class Solution:
    def productExceptSelf(self,nums: List[int] ):
        left = [1] * len(nums)
        right = [1] * len(nums)
        # left[0] = 1
        for i in range(1,len(nums)):
            left[i] = left[i-1] * nums[i-1]  
            # print(left)

        for j in range(len(nums ) -2,-1,-1):
            right[j] = right[j+1] * nums[j+1]
            # print(right)

        res = []
        for k in range(len(left)):
            new = left[k] * right[k]
            res.append(new)
        return res

        


solution = Solution()
print(solution.productExceptSelf(nums))