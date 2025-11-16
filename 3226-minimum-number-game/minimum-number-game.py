class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        temp_arr = []
        result = []
        for index, num in enumerate(sorted_nums):
            temp_arr.append(num)
            if (index + 1) % 2 == 0:
                temp_arr.reverse()
                result.extend(temp_arr)
                temp_arr = []
        return result