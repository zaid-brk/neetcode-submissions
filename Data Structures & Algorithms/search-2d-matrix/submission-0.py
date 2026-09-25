class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # 2d int array matrix -> int target 
        # sorted in increasing order 
        # first int of every row is greater than the last int of prev row
        # true if target exists

        # brainstorming: 
        # brute force: loop thru the entire matrix each time 
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            for j in range(c): 
                if matrix[i][j] == target:
                    return True
        
        return False
        