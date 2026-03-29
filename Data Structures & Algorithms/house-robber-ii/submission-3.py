class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_line(arr):
            prev, curr = 0, 0
            for x in arr:
                prev, curr = curr, max(prev + x, curr)
            return curr

        if len(nums) == 1:
            return nums[0]

        return max(rob_line(nums[:-1]),
                   rob_line(nums[1:]))
