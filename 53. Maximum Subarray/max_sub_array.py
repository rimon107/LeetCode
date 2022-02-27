from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_slice = max_ending = 0
        
        for num in nums:
            max_ending = max(0, max_ending+num)
            max_slice = max(max_slice, max_ending)
        if max_slice==0:
            return max(nums)
        return max_slice