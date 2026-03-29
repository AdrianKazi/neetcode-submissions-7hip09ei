class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        while matrix:
            # whole first row
            if matrix: 
                res.extend(matrix.pop(0))

            # last indexes from all rows from top to bottom
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())

            # last row reversed
            if matrix:
                res.extend(matrix.pop()[::-1])

            # first indexes from all rows from bootom to top
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))

        return res