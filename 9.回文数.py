#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        if x < 10:
            return True
        str_x = str(x)
        if str_x[::-1] == str_x:
            return True
        return False
# @lc code=end

