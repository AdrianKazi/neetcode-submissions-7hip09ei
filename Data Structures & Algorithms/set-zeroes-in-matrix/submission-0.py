class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        zero_row = []
        zero_col = []

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):

                if matrix[row][col] == 0:

                    zero_row.append(row)
                    zero_col.append(col)
            
        for row, col in zip(zero_row, zero_col):
            # zero the row
            matrix[row] = [0]*len(matrix[0])

            # zero the col
            for row_int in range(len(matrix)):
                matrix[row_int][col] = 0
        
