class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        
        for v in collections.Counter(s).values():
            counter += v // 2 * 2
            if(counter % 2 == 0 and v % 2 == 1):
                counter += 1
        return counter
