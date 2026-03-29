class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "":
            return 0

        unique = []
        curr_max_len = 0
        total_max_len = 0
        
        for i in range(len(s)):
            if s[i] not in unique: 
                unique.append(s[i])
                curr_max_len += 1
            else:
                # we take valid letters from last unique letters list
                unique = unique[unique.index(s[i])+1:]
                # we add letter that broke the string
                unique.append(s[i])
                curr_max_len = len(unique)

            total_max_len = max(total_max_len, curr_max_len)
            
        return total_max_len


