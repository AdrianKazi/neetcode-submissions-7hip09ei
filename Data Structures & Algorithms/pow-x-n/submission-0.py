class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0

        res = 1
        for _ in range(abs(n)):
            res *= x
            print(res)
        if n > 0:
            return res
        if n < 0:
            return 1/res

