class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_cont = 0
        l, r = 0, len(heights) - 1

        while l < r:
            cont = abs(l - r) * min(heights[l], heights[r])
            max_cont = max(max_cont, cont)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_cont
