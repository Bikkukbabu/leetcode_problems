import math


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        large_diagonal= 0
        result = 0
        for l, w in dimensions:
            diagonal_length = math.sqrt(l*l+w*w)
            if diagonal_length>large_diagonal:
                large_diagonal = diagonal_length
                result = l*w
            if  diagonal_length == large_diagonal:
                result = max(result, l*w)
        return result