class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        p = 0
        for i in range(n-1,0,-1):
            if nums[i - 1] < nums[i]:
                p = i
                break
        if p == 0:
            nums.sort()
            return
        swap = n - 1
        while nums[p-1] >= nums[swap]:
            swap -= 1
        nums[swap],nums[p-1] = nums[p-1], nums[swap]
        nums[p:] = sorted(nums[p:])
