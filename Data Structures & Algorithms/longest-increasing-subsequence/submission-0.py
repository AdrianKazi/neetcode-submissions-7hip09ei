class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums) # dlugosc najdluzszej rosnacej subsekwencji ktora kocnzy sie na nums[i]

        for i in range(len(nums)): # od 0 do konca
            for j in range(i): # od 0 do i
                if nums[j] < nums[i]: # jezeli wpada w subsekwencje rosnaca
                    dp[i] = max(dp[i], dp[j] + 1) # dp[j]+1 to obecna subsekwencja wiec +1, chodzi o to ze pomiedzy j a i moze byc mniejsza liczba niz ostatnia w subsekwencji do j, i moze przerwac subsekwencje, wtedy dp[i] bedzie mozliwe ze mniejsze niz dp[j]

        return max(dp) # zwroc najwieksza subsekwencje

