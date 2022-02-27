class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, base=2)
        b = int(b, base=2)
        res_bin = bin(a+b)
        return res_bin[2:]