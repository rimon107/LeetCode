from add_two_numbers import Solution

class TestAddTwoNumbers:
    def test_add_two_numbers_1(self):
        list_1, list_2 = [2,4,3], [5,6,4]
        sol_node = [7, 0, 8]
        not_sol_node = [7, 1, 8]
        solution = Solution()

        l1 = solution.create_list_node(list_1)
        l2 = solution.create_list_node(list_2)
        sol_list = solution.create_list_node(sol_node)
        not_sol_list = solution.create_list_node(not_sol_node)

        result = solution.addTwoNumbers(l1, l2)
        
        assert result==sol_list
        assert result!=not_sol_list

    def test_add_two_numbers_2(self):
        list_1, list_2 = [9,9,9,9,9,9,9], [9,9,9,9]
        sol_node = [8,9,9,9,0,0,0,1]
        not_sol_node = [8,9,9,9,0,0,0,0]
        solution = Solution()

        l1 = solution.create_list_node(list_1)
        l2 = solution.create_list_node(list_2)
        sol_list = solution.create_list_node(sol_node)
        not_sol_list = solution.create_list_node(not_sol_node)

        result = solution.addTwoNumbers(l1, l2)
        
        assert result==sol_list
        assert result!=not_sol_list
    
    def test_add_two_numbers_3(self):
        list_1, list_2 = [0], [0]
        sol_node = [0]
        not_sol_node = [1]
        solution = Solution()

        l1 = solution.create_list_node(list_1)
        l2 = solution.create_list_node(list_2)
        sol_list = solution.create_list_node(sol_node)
        not_sol_list = solution.create_list_node(not_sol_node)

        result = solution.addTwoNumbers(l1, l2)
        
        assert result==sol_list
        assert result!=not_sol_list
    
    def test_add_two_numbers_4(self):
        list_1, list_2 = [5], [5]
        sol_node = [0, 1]
        not_sol_node = [1, 1]
        solution = Solution()

        l1 = solution.create_list_node(list_1)
        l2 = solution.create_list_node(list_2)
        sol_list = solution.create_list_node(sol_node)
        not_sol_list = solution.create_list_node(not_sol_node)

        result = solution.addTwoNumbers(l1, l2)
        
        assert result==sol_list
        assert result!=not_sol_list
