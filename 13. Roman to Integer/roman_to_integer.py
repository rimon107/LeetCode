
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        flag = False

        for i, char in enumerate(s):
            if flag:
                flag = False
                continue
            if i+1 < len(s):
                next_char = s[i+1]
                if char=="I":
                    if next_char=="V":
                        res += 4
                        flag = True
                    elif next_char=="X":
                        res += 9
                        flag = True
                    else:
                        res += roman_int[char]
                elif char=="X":
                    if next_char=="L":
                        res += 40
                        flag = True
                    elif next_char=="C":
                        res += 90
                        flag = True
                    else:
                        res += roman_int[char]
                elif char=="C":
                    if next_char=="D":
                        res += 400
                        flag = True
                    elif next_char=="M":
                        res += 900
                        flag = True
                    else:
                        res += roman_int[char]
                else:
                    res += roman_int[char]
            else:
                res += roman_int[char]

        return res
