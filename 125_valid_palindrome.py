class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([el.lower() for el in s if el and el.isalnum()])
        start, end = 0, len(s)-1
        while start<end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
