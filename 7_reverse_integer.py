class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        
        num = 0
        a = abs(x)
        
        while (a != 0):
            temp = a % 10
            num = num * 10 + temp
            a = a // 10
            
        if (x > 0 and num < math.pow(2, 31) -1):
            return num
        elif (x < 0 and num <= math.pow(2, 31) - 1):
            return -num
        else:
            return 0
