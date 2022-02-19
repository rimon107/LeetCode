import remove_element

def test_remove_element_1():
    solution = remove_element.Solution()
    nums, target = [3,2,2,3], 3
    result = solution.removeElement(nums, target)
    assert result==2

def test_remove_element_2():
    solution = remove_element.Solution()
    nums, target = [0,1,2,2,3,0,4,2], 2
    result = solution.removeElement(nums, target)
    assert result==5
