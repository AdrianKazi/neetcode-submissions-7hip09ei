class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prods = []

        for i in range(len(nums)):
            
            left = nums[0:i]
            right = nums[i+1:]

            prod_left = 1
            prod_right = 1
            for j in range(len(left)):
                prod_left *= left[j]
            
            for k in range(len(right)):
                prod_right *= right[k]

            prods.append(prod_left * prod_right)

        return prods
