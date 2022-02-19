from lswrc import Solution

class TestLSWRC:
    def test_lswrc_1(self):
        s = "abcabcbb"
        output = 3
        solution = Solution()

        result = solution.lengthOfLongestSubstring(s)
        assert result==output

    def test_lswrc_2(self):
        s = "bbbbbbbbbbbb"
        output = 1
        solution = Solution()

        result = solution.lengthOfLongestSubstring(s)
        assert result==output

    def test_lswrc_3(self):
        s = "pwwkew"
        output = 3
        solution = Solution()

        result = solution.lengthOfLongestSubstring(s)
        assert result==output

    def test_lswrc_4(self):
        s = " "
        output = 1
        solution = Solution()

        result = solution.lengthOfLongestSubstring(s)
        assert result==output

    def test_lswrc_5(self):
        s = "dvdf"
        output = 3
        solution = Solution()

        result = solution.lengthOfLongestSubstring(s)
        assert result==output