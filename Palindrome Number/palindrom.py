
class Solution:
    def isPalindromeStr(self, x: int) -> bool:
        a = str(x)
        b = "".join(reversed(a))
        
        if a==b:
            return True
        return False
    
    def isPalindromeInt(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse = 0
        num = x
        while num>0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10
        if x==reverse:
            return True
        return False
    
    def isPalindrome(self, x: int) -> bool:
        # res_str = self.isPalindromeStr(x)
        res_int = self.isPalindromeInt(x)
        return res_int
        
        
        