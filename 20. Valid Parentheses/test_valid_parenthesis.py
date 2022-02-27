from valid_parenthesis import Solution

class TestValidParenthesis:
    def test_valid_parenthesis_1(self):
        s = "()"
        output = True
        solution = Solution()

        result = solution.isValid(s)
        assert result==output
    
    def test_valid_parenthesis_2(self):
        s = "()[]{}"
        output = True
        solution = Solution()

        result = solution.isValid(s)
        assert result==output
    
    def test_valid_parenthesis_3(self):
        s = "(]"
        output = False
        solution = Solution()

        result = solution.isValid(s)
        assert result==output

    def test_valid_parenthesis_4(self):
        s = "(("
        output = False
        solution = Solution()

        result = solution.isValid(s)
        assert result==output
    
    def test_valid_parenthesis_5(self):
        s = "]"
        output = False
        solution = Solution()

        result = solution.isValid(s)
        assert result==output
