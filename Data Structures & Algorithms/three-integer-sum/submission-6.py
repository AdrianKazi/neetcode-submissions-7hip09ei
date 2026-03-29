class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        elif len(nums) == 3 and sum(nums) != 0:
            return []
        elif len(nums) == 3 and sum(nums) == 0:
            return [nums]

        res = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = sorted([nums[i],nums[j],nums[k]])
                        if temp not in res:
                            res.append(temp)
        
       
        return res