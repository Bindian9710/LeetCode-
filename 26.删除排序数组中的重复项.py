#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        new_index = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[new_index]:
                new_index += 1
                nums[new_index] = nums[i]
        return new_index+1

# @lc code=end

