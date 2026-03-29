class Solution:
    def rob(self, nums: List[int]) -> int:
        
        h1 = 0
        h2 = 0

        for num in nums:
            h3 = max(h1 + num, h2)
            h1 = h2
            h2 = h3

        return h2
