class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_mapping = {}
        for num in nums:
            if num in nums_mapping:
                return True
            else:
                nums_mapping[num] = 1
        return False