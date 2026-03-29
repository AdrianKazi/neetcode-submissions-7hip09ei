class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_sub = nums[0]
        min_sub = nums[0]
        result  = nums[0]

        for n in nums[1:]:
            if n < 0:
                max_sub, min_sub = min_sub, max_sub

            max_sub = max(n, max_sub * n)
            min_sub = min(n, min_sub * n)

            result = max(result, max_sub)

        
        return result

        