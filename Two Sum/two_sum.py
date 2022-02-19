from sys import maxsize
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        
        for i, num in enumerate(nums):
            num_dict[num] = i
        
        for i, num in enumerate(nums):
            find = target - nums[i]
            if find in num_dict:
                if i==num_dict[find]:
                    continue
                return [i, num_dict[find]]