class Solution:
    def search(self, nums: List[int], target: int) -> int:
        array_len = len(nums)
        mid_point = array_len//2
        if target == nums[mid_point-1]:
            return 0 if mid_point == 0 else mid_point-1
        elif target<nums[mid_point]:
            lower = 0
            upper = mid_point - 1
        else:
            lower = mid_point
            upper = array_len - 1
        for i in range(lower, upper+1):
            if target == nums[i]:
                return i
        return -1
        