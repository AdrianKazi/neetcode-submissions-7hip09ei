class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 1st row - goes fully
        # 2nd to n-1 rows - goes last indx
        # nth row - goes fully in reverse
        # n-1 to 2nd rows - gos first indx

        res = []

        while matrix:
            # 1st row
            res.extend(matrix.pop(0))

            # last idx
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())

            #  nth row in rev
            if matrix:
                res.extend(matrix.pop()[::-1])

            # first idx
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))

        return res