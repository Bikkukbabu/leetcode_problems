class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0
        digits = []
        for num in nums:
            element_sum = element_sum + num
            if num <= 9:
                digit_sum = digit_sum + num
                continue
            while num > 0:
                digit = num % 10
                digit_sum = digit_sum + digit
                num = num//10
        return abs(element_sum-digit_sum)
        