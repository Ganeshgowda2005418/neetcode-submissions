class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                if target==matrix[i][j]:
                    return True
        return False