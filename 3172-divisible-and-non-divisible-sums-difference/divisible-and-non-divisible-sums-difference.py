class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible_sum = 0
        not_divisible_sum = 0
        for num in range(1, n+1):
            if num%m == 0:
                divisible_sum+=num
            else:
                not_divisible_sum+=num
        return not_divisible_sum-divisible_sum