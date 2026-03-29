class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_cont = 0

        for i in range(len(heights)):
            for j in range(i, len(heights)):
                cont = abs(i - j) * min(heights[i], heights[j])
                max_cont = max(max_cont, cont)

        return max_cont
