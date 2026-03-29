class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prods = []
        
        for i in range(len(nums)):

            curr = nums.pop(i)

            prod = math.prod(nums)
            prods.append(prod)

            nums.insert(i, curr)

        return prods
        

            