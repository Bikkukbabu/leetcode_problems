class Solution:
    def isHappy(self, n: int) -> bool:
        s = 0
        squares = set()
        while n!=0:
            d = n%10
            s = s+d*d
            n = n//10
            if n!=0:
                continue
            if s==1:
                return True
            if s in squares:
                return False
            squares.add(s)
            n = s
            s = 0
