class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        shortest_str = strs[0]

        for i in range(1,len(strs)):
            if len(strs[i]) < len(shortest_str):
                shortest_str = strs[i]

        i = 0
        while i < len(strs):
            if shortest_str not in strs[i]:
                shortest_str = shortest_str[:-1]
                i -= 1
            i += 1

        
        return shortest_str