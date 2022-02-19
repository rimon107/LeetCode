class Solution:
    def reverse(self, x: int) -> int:
        max_limit = (1 << 31) -1
        min_limit = (-1) * (1 << 31) 

        sign = 1 if x > 0 else -1
        reverse = 0
        x *= sign
        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10
        
        if reverse > max_limit or reverse < min_limit:
            return 0
        
        return reverse * sign

        