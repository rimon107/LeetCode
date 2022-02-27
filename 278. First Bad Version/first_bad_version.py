# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def __init__(self, bad):
        self.bad = bad

    def isBadVersion(self, bad:int) -> bool:
        return bad>=self.bad

    def firstBadVersion(self, n: int) -> int:
        if n==1:
            return 1
        i = -1
        # n -= 1
        flag = False
        while True:
            mid = (i+n) // 2
            if self.isBadVersion(mid):
                n = mid
                if not self.isBadVersion(n-1):
                    return n 
            else:
                i = mid
                if self.isBadVersion(i+1):
                    return i+1 
            
        