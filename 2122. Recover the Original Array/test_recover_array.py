from recover_array import Solution

class TestRecoverArray:
    def test_recover_array_1(self):
        nums = [2,10,6,4,8,12]
        output = [3,7,11]
        solution = Solution()

        result = solution.recoverArray(nums)
        assert result==output

    def test_recover_array_2(self):
        nums = [1,1,3,3]
        output = [2,2]
        solution = Solution()

        result = solution.recoverArray(nums)
        assert result==output

    def test_recover_array_3(self):
        nums = [5,435]
        output = [220]
        solution = Solution()

        result = solution.recoverArray(nums)
        assert result==output

    # def test_recover_array_4(self):
    #     nums = [11,6,3,4,8,7,8,7,9,8,9,10,10,2,1,9]
    #     output = [2,3,7,8,8,9,9,10]
    #     solution = Solution()

    #     result = solution.recoverArray(nums)
    #     assert result==output

    