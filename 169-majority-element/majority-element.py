import math


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_mapping = {}
        num_half_len = math.ceil(len(nums)/2)
        for num in nums:
            num_mapping[num] = num_mapping.get(num, 0) + 1
            if num_mapping[num] >= num_half_len:
                return num