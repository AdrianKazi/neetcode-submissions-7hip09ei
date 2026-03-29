class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k
        res = []

        while r <= len(nums):
            max_num = max(nums[l:r])
            res.append(max_num)
            l += 1
            r += 1

        return res

