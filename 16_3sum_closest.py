class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return -1 
        
        nums.sort()
        ans = None
        
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if ans is None or abs(s - target) < abs(ans - target):
                    ans = s
                if s < target:
                    l += 1
                else:
                    r -= 1
        return ans
