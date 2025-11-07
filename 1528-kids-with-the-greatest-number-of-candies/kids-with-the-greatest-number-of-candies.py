class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        temp = 0
        for candie_count in candies:
            temp = candie_count
            if temp + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
            temp = 0
        return result