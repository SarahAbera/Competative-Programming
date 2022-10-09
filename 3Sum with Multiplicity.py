class Solution(object):
    def threeSumMulti(self, arr, target):
        count = [0]*101
        result,mod = 0,10**9+7
        for i in arr: count[i] += 1
        
        for i in range (101):
            for j in range(i, 101):
                k = target - i - j
                if not (0 <= k <= 100): 
                    continue
                elif i == j == k:
                    result += (count[i] * (count[i]-1) * (count[i] - 2) // 6)
                elif i == j != k:
                    result += (count[k] * (count[i] * (count[i]-1) // 2))
                elif i < j < k:
                    result += (count[i] * count [j] * count [k])
        return result % mod
        
