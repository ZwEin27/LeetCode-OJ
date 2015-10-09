class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # https://en.wikipedia.org/wiki/Digital_root
        if num == 0:
             return 0;  
        if num % 9 == 0:
            return 9;  
        return num % 9;