from integer_to_roman import Solution

class TestIntegerToRoman:
    def test_integer_to_roman_1(self):
        num = 3
        output = "III"
        solution = Solution()

        result = solution.intToRoman(num)
        assert result==output
    
    def test_integer_to_roman_2(self):
        num = 58
        output = "LVIII"
        solution = Solution()

        result = solution.intToRoman(num)
        assert result==output
    
    def test_integer_to_roman_3(self):
        num = 1994
        output = "MCMXCIV"
        solution = Solution()

        result = solution.intToRoman(num)
        assert result==output
