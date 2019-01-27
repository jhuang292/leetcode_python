class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        if not nums:
            return 0
        
        index, dic = 0, {}
        for item in nums:
            if item not in dic:
                dic[item] = 1 
                nums[index] = item
                index += 1 
        return index
