class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1
        num = 0
        max_limit = (1 << 31) - 1
        min_limit = (-1) * (1 << 31)
        if len(s) > 0:
            sign_letter = s[0]
            if sign_letter=="+" or sign_letter=="-":
                sign = 1 if sign_letter=="+" else -1
                s = s[1:]
            for letter in s:
                if letter.isdigit():
                    num = num * 10 + int(letter)
                    continue
                break
        num = num * sign
        if num > max_limit:
            num = max_limit
        if num < min_limit:
            num = min_limit
        return num
                