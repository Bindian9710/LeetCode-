#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits):
        dig = int(''.join(str(i) for i in digits))+1
        return [int(i) for i in list(str(dig))]
# @lc code=end

