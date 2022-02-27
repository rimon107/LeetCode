class Solution:
    def myPow(self, x: float, n: int) -> float:
        x_sign = 1
        if x < 0:
            x_sign = -1
            x = x * -1
        
        n_sign = 1
        if n < 0:
            n_sign = -1
            n = n * -1
        
        if n%2==0:
            x_sign = 1
            
        ans = 1
        while n > 0:
            last_bit = n&1
            
            if last_bit:
                ans *= x
            
            x *= x
            n = n >> 1
        
        if n_sign==-1:
            ans = (1 / ans)
        
        return ans * x_sign
        