class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers or len(numbers) < 2:
            return -1
        l, r = 0, len(numbers) - 1
        for i in range(r):
            while l < r and numbers[l] + numbers[r] < target:
                l += 1
            if l != r and numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            r -= 1
        return -1
