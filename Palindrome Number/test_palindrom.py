from palindrom import Solution

class TestPalindrom:
    def test_palindrom_1(self):
        x, sol = 121, True
        solution = Solution()
        result = solution.isPalindrome(x)
        
        assert result==sol

    def test_palindrom_2(self):
        x, sol = -121, False
        solution = Solution()
        result = solution.isPalindrome(x)
        
        assert result==sol
