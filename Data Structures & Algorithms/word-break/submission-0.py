class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # dp[i] tells us if substring s[i:] can be built from wordDict
        dp[len(s)] = True # empty suffix is True

        for i in range(len(s) - 1, -1, -1): # going from back in s
            for w in wordDict: # going forward with each w
                if s[i:i+len(w)] == w:
                    if dp[i + len(w)]:
                        dp[i] = True
                        break
        
        return dp[0]