from permutation_sequence import Solution

class TestPermutationSequence:
    def test_permutation_sequence_1(self):
        n, k = 3, 3
        output = "213"
        solution = Solution()
        res = solution.getPermutation(n, k)
        assert res==output

    def test_first_bad_version_2(self):
        n, k = 4, 9
        output = "2314"
        solution = Solution()
        res = solution.getPermutation(n, k)
        assert res==output

    def test_first_bad_version_3(self):
        n, k = 3, 1
        output = "123"
        solution = Solution()
        res = solution.getPermutation(n, k)
        assert res==output