from typing import List


class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        n = len(nums) // 2
        # nums.sort()
        lower = nums[0:n]     
        higher = nums[n:n*2]
        res = []
        lower.sort()
        higher.sort()
        for i in range(n):
            total = lower[i]+higher[i]
            if total % 2 == 1:
                total += 1
            num = total // 2
            res.append(num)
        res.sort()
        return res