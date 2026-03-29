class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n

        prev = 1
        curr = 2

        for _ in range(3, n+1):
            new  = prev + curr
            prev = curr
            curr = new

        return curr


        

       