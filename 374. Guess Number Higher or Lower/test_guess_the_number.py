from guess_the_number import Solution

class TestGuessNumber:
    def test_guess_the_number_1(self):
        n, pick = 10, 6
        output = 6
        solution = Solution(pick)
        res = solution.guessNumber(n)
        assert res==output

    def test_guess_the_number_2(self):
        n, pick = 3, 2
        output = 2
        solution = Solution(pick)
        res = solution.guessNumber(n)
        assert res==output

    def test_guess_the_number_3(self):
        n, pick = 2, 1
        output = 1
        solution = Solution(pick)
        res = solution.guessNumber(n)
        assert res==output