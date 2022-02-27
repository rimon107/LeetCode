# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def __init__(self, pick):
        self.pick = pick

    def guess(self, pick: int) -> bool:
        if pick == self.pick:
            return 0
        if pick > self.pick:
            return -1
        if pick < self.pick:
            return 1

    def guessNumber(self, n: int) -> int:
        if self.guess(n)==0:
            return n
        i = 0
        h = n
        
        while True:
            mid = (i+h) // 2
            pick = self.guess(mid)

            if pick==0:
                return mid
            
            if pick==-1:
                h = mid
            elif pick==1:
                i = mid
            
        