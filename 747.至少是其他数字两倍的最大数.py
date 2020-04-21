#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums) -> int:
        max_num = max(nums)
        if all(max_num >= i*2 for i in nums if i != max_num):
            return nums.index(max_num)
        return -1

# print(Solution().dominantIndex([0,0,0,1]))

# @lc code=end

