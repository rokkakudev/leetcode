from solution import Solution


class TestBasicCases:
    def test_solution_at_head_elements(self):
        nums = [2, 7, 11, 15]
        target = 9

        result = Solution().twoSum(nums, target)

        assert result == [0, 1]

    def test_solution_at_tail_elements(self):
        nums = [3, 2, 4]
        target = 6

        result = Solution().twoSum(nums, target)

        assert result == [1, 2]

    def test_solution_at_separated_elements(self):
        nums = [4, 5, 6]
        target = 10

        result = Solution().twoSum(nums, target)

        assert result == [0, 2]


class TestValueProperties:
    def test_negative_numbers(self):
        nums = [-3, 1, 8]
        target = 5

        result = Solution().twoSum(nums, target)

        assert result == [0, 2]

    def test_zero_elements(self):
        nums = [0, 2, 5]
        target = 2

        result = Solution().twoSum(nums, target)

        assert result == [0, 1]

    def test_duplicate_values(self):
        nums = [3, 3]
        target = 6

        result = Solution().twoSum(nums, target)

        assert result == [0, 1]

    def test_large_numbers(self):
        nums = [10**100, 10**18]
        target = 10**100 + 10**18

        result = Solution().twoSum(nums, target)

        assert result == [0, 1]


class TestArraySizes:
    def test_minimum_array_size(self):
        nums = [1, 2]
        target = 3

        result = Solution().twoSum(nums, target)

        assert result == [0, 1]

    def test_large_array_correctness(self):
        size = 10_000

        nums = list(range(size))
        target = (size - 2) + (size - 1)

        result = Solution().twoSum(nums, target)

        assert result == [size - 2, size - 1]
