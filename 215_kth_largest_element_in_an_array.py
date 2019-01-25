class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
        return self.quickSelect(nums, 0, len(nums) - 1, k)
    
    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        
        i, j = start, end
        pivot = nums[(i + j) // 2]
        
        while i <= j:
            while i <= j and nums[i] > pivot:
                i += 1
            while i <= j and nums[j] < pivot:
                j -= 1
            if i <= j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j -= 1
        
        if start + k - 1 <= j:
            return self.quickSelect(nums, start, j, k)
        if start + k - 1 >= i:
            return self.quickSelect(nums, i, end, k - (i - start))
        return nums[j + 1]
