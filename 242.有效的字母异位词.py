#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_v = {}
        for k,v in zip(list(s),list(t)):
            if k not in dict_s:
                dict_s[k] = 1
            else:
                dict_s[k] -= 1
            if v not in dict_v:
                dict_v[v] = 1
            else:
                dict_v[v] -= 1
        print(dict_s,dict_v)
        return dict_s == dict_v
        
# @lc code=end

