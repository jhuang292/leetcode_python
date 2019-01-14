class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if (len(nums) == 0):
            return [-1,-1]
        
        bound = []
        start, end = 0, len(nums)-1
        while (start + 1 < end):
            mid = start + (end-start) // 2
            if (nums[mid] == target):
                end = mid
            elif (nums[mid] < target):
                start = mid
            else:
                end = mid
        if (nums[start] == target):
            bound.append(start)
        elif (nums[end] == target):
            bound.append(end)
        else:
            bound = [-1,-1]
            return bound
        
        start, end = 0, len(nums)-1
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if (nums[mid] == target):
                start = mid
            elif (nums[mid] < target):
                start = mid
            else:
                end = mid
        if (nums[end] ==  target):
            bound.append(end)
        elif (nums[start] == target):
            bound.append(start)
        else:
            bound = [-1,-1]
            return bound
        return bound
            
        
