# question : find the smallest  element of the number which is greater to or equal the target
# like if taget is 15 then it shoud give 16 because all of the element larger than the arr the 16 is shortes of them all

arr = [2,3,5,9,14,16,18 ]

target = 3

from typing import List

class Solution():
    def ceiling(self,arr,target):
        start = 0
        stop = len(arr) - 1
        res = None
        while stop >= start:
            mid = (start + stop) // 2
            if arr[mid] == target:
                return (arr[mid])
            elif arr[mid] < target:
                start = mid + 1
                # res.append(arr[mid])
            else:
                res = arr[mid]
                stop = mid - 1
                
        return res
    
solution = Solution()
result = solution.ceiling(arr,target)
print(result)

