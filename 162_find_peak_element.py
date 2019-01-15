class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1 
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid - 1] < nums[mid] and nums[mid] < nums[mid + 1]:
                start = mid
            elif nums[mid + 1] < nums[mid] and nums[mid] < nums[mid - 1]:
                end = mid
            else:
                end = mid
        if nums[start] > nums[end]:
            return start
        else:
            return end
            
        
