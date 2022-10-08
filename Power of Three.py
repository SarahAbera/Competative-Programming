326. Power of Three
class Solution(object):
    def isPowerOfThree(self, n):
        if n < 1:
            return False
        if n % 3 != 0 and n != 1:
            return False
        if n == 1:
            return True
        return self.isPowerOfThree(n//3)
