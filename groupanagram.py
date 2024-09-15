# Given an array of strings strs, group all anagrams together into sublists.
# You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, 
# but the order of the characters can be different.

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
from collections import defaultdict
strs = ["act","pots","tops","cat","stop","hat"]

from typing import List 

class Solution:
    def groupAnag(self,strs: List[str]):
        ans = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord("a")] += 1
            ans[tuple(count)].append(i)
            # print(ans)
        return list[ans.values()]
                

solution = Solution()
result = solution.groupAnag(strs)
print(result)
