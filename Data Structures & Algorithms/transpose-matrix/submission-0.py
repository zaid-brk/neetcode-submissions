class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])

        transp = []
        for i in range(c):
            new_row = [0] * r
            transp.append(new_row)

        for j in range(r):
            for k in range(c):
                transp[k][j] = matrix[j][k]
 
        return transp
