from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                k += 1
                nums[i] = 10000
        nums.sort()
        return len(nums)-k
        