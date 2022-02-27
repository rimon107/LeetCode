class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend_sign = 1
        if dividend < 0:
            dividend_sign = -1
            dividend = dividend * -1
            
        divisor_sign = 1
        if divisor < 0:
            divisor_sign = -1
            divisor = divisor * -1
            
        
        quo, _ = divmod(dividend, divisor)
        quo = quo * dividend_sign * divisor_sign
        if quo >= (1 << 31):
            quo = (1 << 31) - 1
        if quo < (1 << 31) * -1:
            quo = (1 << 31) * -1
        
        return quo
        