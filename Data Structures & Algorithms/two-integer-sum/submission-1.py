class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force O(n^2)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i!=j and nums[i] + nums[j] == target:
        #             return [i, j]

        # Hash Map (One Pass)
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
