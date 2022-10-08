189. Rotate Array

class Solution(object):
    def rotate(self, nums, k):
        a = k % len(nums)
        l = len(nums) - a
        for i in range(l):
            nums.append(nums[0])
            nums.pop(0)
        return nums 
