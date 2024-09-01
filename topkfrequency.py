# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
from typing import List

nums = [1,1,1,2,2,3]
k = 2

class Solution:
    def topkfreq(self,k: int, nums: List[int]):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num,0)
        for n,c in count.items():
            freq[c].append(n)
        # return freq
        res = []
        for i in range(len(freq) -1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) >= k:
                    return res

            

solution = Solution()
print(solution.topkfreq(k,nums))