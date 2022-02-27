from first_bad_version import Solution

class TestFirstBadVersion:
    def test_first_bad_version_1(self):
        n, bad = 5, 4
        output = 4
        solution = Solution(bad)
        res = solution.firstBadVersion(n)
        assert res==output

    def test_first_bad_version_2(self):
        n, bad = 1, 1
        output = 1
        solution = Solution(bad)
        res = solution.firstBadVersion(n)
        assert res==output

    def test_first_bad_version_3(self):
        n, bad = 2, 1
        output = 1
        solution = Solution(bad)
        res = solution.firstBadVersion(n)
        assert res==output