from max_sub_array import Solution


class TestMaxSubArray:
    def test_max_sub_array_1(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        output = 6
        solution = Solution()
        res = solution.maxSubArray(nums)
        assert res==output
    
    def test_max_sub_array_2(self):
        nums = [-1]
        output = -1
        solution = Solution()
        res = solution.maxSubArray(nums)
        assert res==output

    def test_max_sub_array_3(self):
        nums = [-1, -2]
        output = -1
        solution = Solution()
        res = solution.maxSubArray(nums)
        assert res==output