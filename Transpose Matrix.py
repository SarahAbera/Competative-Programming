class Solution(object):
    def transpose(self, matrix):
        m, n = len(matrix), len(matrix[0])
        res = [[] * m for i in range(n)]
        for i in range(n):
            for j in range(m):   
                res[i].append(matrix[j][i])
        return res
