class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        zadanie to glownie rozkminienie jak poradzic sobie z "-" bo gdyby nie one to zawsze caly array daje najwiekszy prod bo mamy liczby calkowite.
        '''
        min_prod = nums[0]
        max_prod = nums[0]
        result=nums[0]

        for n in nums[1:]:

            if n < 0:
                min_prod, max_prod = max_prod, min_prod

            max_prod = max(n, max_prod*n)
            min_prod = min(n, min_prod*n)

            result = max(result, max_prod)

        return result