#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target: int):
        hash_map = {}
        for j,i in enumerate(nums):
            if i not in hash_map:
                hash_map[target-i] = j
            else:
                return hash_map[i],j
        return -1,-1              

# @lc code=end

