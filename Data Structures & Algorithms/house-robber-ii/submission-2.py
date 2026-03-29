class Solution:
    def rob(self, nums: List[int]) -> int:

        def robber(arr):
            prev, curr = 0, 0
            for x in arr:
                prev, curr = curr, max(prev + x, curr)
            return curr

        if len(nums) == 1:
            return nums[0]

        return max(
                   robber(nums[:-1]),
                   robber(nums[1:])
                   )
