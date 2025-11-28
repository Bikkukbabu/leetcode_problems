class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        a, b = 0, 1
        i = 0
        while i<=n-2:
            a, b = b, a+b
            i = i+1
        return b