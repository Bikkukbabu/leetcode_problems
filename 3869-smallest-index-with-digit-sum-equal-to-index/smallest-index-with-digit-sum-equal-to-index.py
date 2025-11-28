class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if nums[i] < 10 and nums[i]==i:
                return i
            digits = [int(d) for d in str(nums[i])]
            if sum(digits) == i:
                return i
        return -1

