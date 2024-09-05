# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Input: s = "racecar", t = "carrace"

# Output: true
s = "care"
t = "race"

class Solution:
    def anagram(self,s: str,t: str):
        res = {}
        res2 = {}
        if len(s) == len(t):
            for i in range(len(s)):
                res[s[i]] = res.get(s[i],0) + 1
                res2[t[i]] = res2.get(t[i],0) + 1
            if res == res2:
                return True
        return False


solution = Solution()
result = solution.anagram(s,t)
print(result)