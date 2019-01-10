class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        nums = 0
        a = abs(x)
        
        while (a != 0):
            temp = a % 10
            nums = nums * 10 + temp
            a = a // 10
            
        if (x >= 0 and x == nums):
            return True
        else:
            return False
