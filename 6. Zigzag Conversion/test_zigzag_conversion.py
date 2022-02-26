from timeit import timeit
from zigzag_conversion import Solution

class TestLongestPanildrom:
    def test_zigzag_conversion_1(self):
        s = "PAYPALISHIRING"
        num_rows = 3
        output = "PAHNAPLSIIGYIR"
        solution = Solution()

        result = solution.convert(s, num_rows)
        assert result==output

    def test_zigzag_conversion_2(self):
        s = "PAYPALISHIRING"
        num_rows = 4
        output = "PINALSIGYAHRPI"
        solution = Solution()

        result = solution.convert(s, num_rows)
        assert result==output

    def test_zigzag_conversion_3(self):
        s = "A"
        num_rows = 1
        output = "A"
        solution = Solution()

        result = solution.convert(s, num_rows)
        assert result==output

    
