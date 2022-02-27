import remove_duplicate

def test_remove_duplicate_1():
    solution = remove_duplicate.Solution()
    nums = [2,2,3,3]
    result = solution.removeDuplicates(nums)
    assert result==2

def test_remove_duplicate_2():
    solution = remove_duplicate.Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    result = solution.removeDuplicates(nums)
    assert result==5
