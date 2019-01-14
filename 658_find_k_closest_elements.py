class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        right = self.find_upper_closest (arr, x)
        left = right - 1
        
        results = []
        for _ in range(k):
            if self.is_left_closer (arr, x, left, right):
                results.append(arr[left])
                left -= 1
            else:
                results.append(arr[right])
                right += 1

        return sorted(results)
        
    def find_upper_closest (self, A, target):
        
        start, end = 0, len(A)-1
        while start + 1 < end:
            mid = (start + end) // 2
            if (A[mid] >= target):
                end = mid
            else:
                start = mid
        
        if A[start] >= target:
            return start
        
        if A[end] >= target:
            return end
        
        return end + 1
    
    def is_left_closer (self, A, target, left, right):
        if left < 0:
            return False
        
        if right >= len(A):
            return True
        
        return target - A[left] <= A[right] - target
