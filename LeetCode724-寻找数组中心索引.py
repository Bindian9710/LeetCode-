class Solution:
    def pivotIndex(self, nums):
        numAll = sum(nums)
        for i in range(len(nums)):
            if sum(nums[:i])*2+nums[i] == numAll:
                return i
        return -1

