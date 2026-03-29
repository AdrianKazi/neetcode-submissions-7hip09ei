class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_loop(nums):
            h1 = 0
            h2 = 0
            for num in nums:
                h3 = max(h1+num, h2)
                h1 = h2
                h2 = h3
            return h2

        return max(rob_loop(nums[:-1]), rob_loop(nums[1:]))