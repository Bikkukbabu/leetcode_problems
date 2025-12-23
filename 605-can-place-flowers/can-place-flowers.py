class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        left_empty = False
        right_empty = False
        planted = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_empty = (i==0 or flowerbed[i-1]==0)
                right_empty = (i==len(flowerbed)-1 or flowerbed[i+1]==0)
                if left_empty and right_empty:
                    planted = planted+1
                    flowerbed[i] = 1
        if planted >= n:
            return True
        return False