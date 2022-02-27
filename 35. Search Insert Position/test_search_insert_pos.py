from search_insert_pos import Solution

class TestSearchInsertPosition:
    def test_search_insert_pos_1(self):
        nums, target = [1,3,5], 4
        output = 2
        solution = Solution()
        res = solution.searchInsert(nums, target)
        assert res==output

    def test_search_insert_pos_2(self):
        nums, target = [1, 3, 5, 7, 9, 11, 13], 4
        output = 2
        solution = Solution()
        res = solution.searchInsert(nums, target)
        assert res==output

    def test_search_insert_pos_3(self):
        nums, target = [1, 3, 5, 7, 9, 11, 13], 10
        output = 5
        solution = Solution()
        res = solution.searchInsert(nums, target)
        assert res==output