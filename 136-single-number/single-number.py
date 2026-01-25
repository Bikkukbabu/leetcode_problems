class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_mapping = {}
        result = []
        for num in nums:
            num_mapping[num] = num_mapping.get(num, 0) + 1
            if num_mapping[num] == 1:
                result.append(num)
            if num_mapping[num] > 1:
                result.remove(num)
        return result[0]