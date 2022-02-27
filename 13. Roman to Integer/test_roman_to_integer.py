from roman_to_integer import Solution

class TestRomanToInteger:
    def test_roman_to_integer_1(self):
        s = "III"
        output = 3
        solution = Solution()

        result = solution.romanToInt(s)
        assert result==output
    
    def test_roman_to_integer_2(self):
        s = "LVIII"
        output = 58
        solution = Solution()

        result = solution.romanToInt(s)
        assert result==output
    
    def test_roman_to_integer_3(self):
        s = "MCMXCIV"
        output = 1994
        solution = Solution()

        result = solution.romanToInt(s)
        assert result==output
