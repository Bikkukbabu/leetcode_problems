class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        reverse_nums = nums[::-1]
        result = [num for num in range(1, k+1)]
        counter = 0
        for num in reverse_nums:
            counter = counter + 1
            if num in result:
                result.remove(num)
            if result == []:
                return counter
        return counter
