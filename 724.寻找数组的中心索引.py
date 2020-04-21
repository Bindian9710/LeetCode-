#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心索引
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        numAll = sum(nums)
        for i in range(len(nums)):
            if sum(nums[:i])*2+nums[i] == numAll:
                return i
        return -1
        
# @lc code=end

