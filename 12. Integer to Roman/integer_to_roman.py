
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_int = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        res = ""

        while num:
            if num >= 1000:
                n = num // 1000
                for i in range(n):
                    res = res + roman_int[1000]
                num = num % 1000
                continue
            if num < 1000 and num >=100:
                n = num // 100
                if n==9:
                    res = res + roman_int[900]
                elif n<9 and n>=5:
                    for i in range(5, n+1, 1):
                        if i==5:
                            res = res + roman_int[500]
                            continue
                        res = res + roman_int[100]
                elif n==4:
                    res = res + roman_int[400]
                elif n<4 and n>=1:
                    for i in range(1, n+1, 1):
                        res = res + roman_int[100]
                num = num % 100
                continue
            if num < 100 and num >=10:
                n = num // 10
                if n==9:
                    res = res + roman_int[90]
                elif n<9 and n>=5:
                    for i in range(5, n+1, 1):
                        if i==5:
                            res = res + roman_int[50]
                            continue
                        res = res + roman_int[10]
                elif n==4:
                    res = res + roman_int[40]
                elif n<4 and n>=1:
                    for i in range(1, n+1, 1):
                        res = res + roman_int[10]
                num = num % 10
                continue
            elif num < 10 and num >=1:
                if num==9:
                    res = res + roman_int[9]
                elif num<9 and num>=5:
                    for i in range(5, num+1, 1):
                        if i==5:
                            res = res + roman_int[5]
                            continue
                        res = res + roman_int[1]
                elif num==4:
                    res = res + roman_int[4]
                elif num<4 and num>=1:
                    for i in range(1, num+1, 1):
                        res = res + roman_int[1]
                num = num // 10
        return res
