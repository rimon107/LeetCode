from reverse_int import Solution

class TestLSWRC:
    def test_reverse_int_1(self):
        x = 123
        output = 321
        solution = Solution()

        result = solution.reverse(x)
        assert result==output

    def test_reverse_int_2(self):
        x = -123
        output = -321
        solution = Solution()

        result = solution.reverse(x)
        assert result==output

    def test_reverse_int_3(self):
        x = 120
        output = 21
        solution = Solution()

        result = solution.reverse(x)
        assert result==output

    def test_reverse_int_4(self):
        x = -120
        output = -21
        solution = Solution()

        result = solution.reverse(x)
        assert result==output

    def test_reverse_int_max_last(self):
        x = 1 << 31 - 1
        output = 0
        solution = Solution()

        result = solution.reverse(x)
        assert result==output

    def test_reverse_int_max(self):
        x = 1 << 31
        output = 0
        solution = Solution()

        result = solution.reverse(x)
        assert result==output
    
    def test_reverse_int_min(self):
        x = ((-1) * (1 << 31)) -1
        output = 0
        solution = Solution()

        result = solution.reverse(x)
        assert result==output