import two_sum

def test_two_sum_1():
    solution = two_sum.Solution()
    nums, target = [2,7,11,15], 9
    result = solution.twoSum(nums, target)
    assert result==[0,1]

def test_two_sum_2():
    solution = two_sum.Solution()
    nums, target = [3,2,4], 6
    result = solution.twoSum(nums, target)
    assert result==[1,2]

def test_two_sum_3():
    solution = two_sum.Solution()
    nums, target = [3,3], 6
    result = solution.twoSum(nums, target)
    assert result==[0,1]