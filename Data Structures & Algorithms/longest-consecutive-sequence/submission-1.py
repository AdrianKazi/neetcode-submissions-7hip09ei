class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()

        if len(nums) == 0:
            return 0

        curr_max_len = 1
        total_max_len = 1

        # idx = 0
        # curr = nums[idx]


        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                curr_max_len += 1
            elif nums[i] == nums[i+1]:
                curr_max_len += 0
            else:
                curr_max_len = 1
            total_max_len = max(total_max_len, curr_max_len)

        return total_max_len
            



