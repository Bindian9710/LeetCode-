class Solution:
    def dominantIndex(self, nums) -> int:
        max_num = max(nums)
        if all(max_num >= i*2 for i in nums if i != max_num):
            return nums.index(max_num)
        return -1