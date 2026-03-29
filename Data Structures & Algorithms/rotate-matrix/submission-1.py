class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # Input:  [[1,2,3],[4,5,6],[7,8,9]]
        # rever:  [[7,8,9],
                #  [4,5,6],
                #  [1,2,3]]
        # symetric [[7,4,1],
                #   [8,5,2],
                #   [9,6,3]]

        # Output: [[7,4,1],
                #  [8,5,2],
                #  [9,6,3]]

        # reverse
        matrix.reverse()
        
        # transpose
        for row in range(len(matrix)):
            for col in range(row+1, len(matrix[0])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]