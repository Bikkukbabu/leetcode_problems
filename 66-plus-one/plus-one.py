class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        len_array = len(digits)
        for i in range(len_array, 0, -1):
            number = number + digits[len_array-i]*(10**(i-1))
        result = [int(d) for d in str(number+1)]
        return result