from string_to_integer import Solution

class TestStringToInteger:
    def test_my_atoi_1(self):
        s = "42"
        output = 42
        solution = Solution()

        result = solution.myAtoi(s)
        assert result==output

    def test_my_atoi_2(self):
        s = "   -42"
        output = -42
        solution = Solution()

        result = solution.myAtoi(s)
        assert result==output

    def test_my_atoi_3(self):
        s = "4193 with words"
        output = 4193
        solution = Solution()

        result = solution.myAtoi(s)
        assert result==output

    def test_my_atoi_4(self):
        s = "-91283472332"
        output = -2147483648
        solution = Solution()

        result = solution.myAtoi(s)
        assert result==output
    
    def test_my_atoi_5(self):
        n = 1 << 31
        s = str(n)
        output = (1 << 31) - 1
        solution = Solution()

        result = solution.myAtoi(s)
        assert result==output

    def test_my_atoi_6(self):
        n = (1 << 31) - 1
        s = str(n)
        output = (1 << 31) - 1
        solution = Solution()

        result = solution.myAtoi(s)
        assert result==output
    
    def test_my_atoi_7(self):
        n = (1 << 31) - 2
        s = str(n)
        output = (1 << 31) - 2
        solution = Solution()

        result = solution.myAtoi(s)
        assert result==output

    def test_my_atoi_9(self):
        n = (-1) * (1 << 31)
        s = str(n)
        output = (1 << 31) * (-1)
        solution = Solution()

        result = solution.myAtoi(s)
        assert result==output

    def test_my_atoi_10(self):
        n = ((-1) * (1 << 31)) - 1
        s = str(n)
        output = (1 << 31) * (-1)
        solution = Solution()

        result = solution.myAtoi(s)
        assert result==output
    
    def test_my_atoi_11(self):
        n = ((-1) * (1 << 31)) + 1
        s = str(n)
        output = ((1 << 31) * (-1)) + 1
        solution = Solution()

        result = solution.myAtoi(s)
        assert result==output
