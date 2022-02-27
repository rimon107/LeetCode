from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            i = nums.index(target)
        except:
            if target < nums[0]:
                return 0
            l = len(nums) - 1
            if target > nums[l]:
                return l + 1
            i = 0
            while True:
                mid = (i+l) // 2
                if target < nums[mid]:
                    l = mid
                else:
                    i = mid
                if i+1==l:
                    return l
        return i
        