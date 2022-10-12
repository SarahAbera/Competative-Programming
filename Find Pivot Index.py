class Solution(object):
    def pivotIndex(self, nums):
        lenOfnums = len(nums)
        if lenOfnums == 0: 
            return -1
        l = [0 for i in range(lenOfnums)]
        r = [0 for i in range(lenOfnums)]
        r[lenOfnums - 1] = nums[lenOfnums - 1]
        for i in range(lenOfnums - 2, -1, -1):
            r[i] = r[i + 1] + nums[i]
        l[0] = nums[0]
        if r[0] == l[0]:
            return 0
        for i in range(1, lenOfnums):
            l[i] = l[i - 1] + nums[i]
            if l[i] == r[i]:
                return i
        return -1
