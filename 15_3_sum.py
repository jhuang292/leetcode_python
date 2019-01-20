class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        length = len(nums)
        
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            l, r = i + 1, length - 1 
            while l < r:
                if nums[l] + nums[r] == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1 
                    r -= 1 
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1 
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1 
                elif nums[l] + nums[r] < target:
                    l += 1 
                else:
                    r -= 1 
        return result
