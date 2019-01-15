class Solution:
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        if len(image) == 0 or len(image[0]) == 0:
            return 0
        
        start, end = y, len(image[0]) - 1
        while start < end:
            mid = start + (end - start) // 2 + 1
            if self.checkColumn(image, mid):
                start = mid
            else:
                end = mid - 1
        right = start
        
        start, end = 0, y
        while start < end:
            mid = start + (end - start) // 2
            if self.checkColumn(image, mid):
                end = mid
            else:
                start = mid + 1
        left = start
        
        start, end = x, len(image) - 1
        while start < end:
            mid = start + (end - start) // 2 + 1
            if self.checkRow(image, mid):
                start = mid
            else:
                end = mid - 1
        down = start
        
        start, end = 0, x
        while start < end:
            mid = start + (end - start) // 2
            if self.checkRow(image, mid):
                end = mid
            else:
                start = mid + 1
        up = start
        
        return (right - left + 1) * (down - up + 1)
        
        
        
    def checkColumn(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return True
        return False
    
    def checkRow(self, image, row):
        for i in range(len(image[0])):
            if image[row][i] == '1':
                return True
        return False
